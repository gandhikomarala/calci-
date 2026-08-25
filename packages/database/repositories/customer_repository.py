from typing import Optional, List, Tuple, Sequence, Dict, Any
import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, or_, and_, desc
from packages.database.models.customers import (
    Customer, CustomerProfile, CustomerUsage, CustomerPayment,
    CustomerSupportTicket, CustomerSubscription, CustomerEvent, CustomerNote, CustomerTag
)
from packages.database.repository import BaseRepository

class CustomerRepository(BaseRepository[Customer]):
    def __init__(self, session: AsyncSession):
        super().__init__(Customer, session)

    async def get_by_code(self, customer_code: str) -> Optional[Customer]:
        stmt = select(Customer).where(Customer.customer_code == customer_code, Customer.is_deleted == False)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def search_customers(
        self,
        skip: int = 0,
        limit: int = 20,
        search: Optional[str] = None,
        region: Optional[str] = None,
        risk_level: Optional[str] = None,
        is_churned: Optional[bool] = None,
        sort_field: str = "created_at",
        sort_order: str = "desc"
    ) -> Tuple[Sequence[Tuple[Customer, Optional[CustomerProfile]]], int]:
        stmt = select(Customer, CustomerProfile).outerjoin(CustomerProfile, CustomerProfile.customer_id == Customer.id).where(Customer.is_deleted == False)

        if search:
            stmt = stmt.where(or_(
                Customer.first_name.ilike(f"%{search}%"),
                Customer.last_name.ilike(f"%{search}%"),
                Customer.email.ilike(f"%{search}%"),
                Customer.customer_code.ilike(f"%{search}%")
            ))
        if region:
            stmt = stmt.where(Customer.region == region)
        if is_churned is not None:
            stmt = stmt.where(Customer.is_churned == is_churned)
        if risk_level:
            stmt = stmt.where(CustomerProfile.risk_level == risk_level)

        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_res = await self.session.execute(count_stmt)
        total = total_res.scalar_one()

        sort_col = getattr(Customer, sort_field, Customer.created_at)
        if sort_order == "desc":
            stmt = stmt.order_by(desc(sort_col))
        else:
            stmt = stmt.order_by(sort_col)

        res = await self.session.execute(stmt.offset(skip).limit(limit))
        return res.all(), total

    async def get_churn_kpis(self) -> Dict[str, Any]:
        total_stmt = select(func.count()).select_from(Customer).where(Customer.is_deleted == False)
        total_res = await self.session.execute(total_stmt)
        total_customers = total_res.scalar_one() or 1

        churned_stmt = select(func.count()).select_from(Customer).where(Customer.is_churned == True, Customer.is_deleted == False)
        churned_res = await self.session.execute(churned_stmt)
        churned_count = churned_res.scalar_one() or 0

        high_risk_stmt = select(func.count()).select_from(CustomerProfile).where(CustomerProfile.risk_level == "HIGH")
        high_risk_res = await self.session.execute(high_risk_stmt)
        high_risk_count = high_risk_res.scalar_one() or 0

        revenue_at_risk_stmt = select(func.sum(CustomerProfile.current_mrr)).where(CustomerProfile.risk_level == "HIGH")
        revenue_res = await self.session.execute(revenue_at_risk_stmt)
        revenue_at_risk = float(revenue_res.scalar_one() or 0.0)

        return {
            "total_customers": total_customers,
            "churned_customers": churned_count,
            "churn_rate": round((churned_count / total_customers) * 100.0, 2),
            "high_risk_count": high_risk_count,
            "revenue_at_risk": round(revenue_at_risk, 2),
        }

    async def get_usage_timeline(self, customer_id: str, days: int = 30) -> Sequence[CustomerUsage]:
        stmt = select(CustomerUsage).where(
            CustomerUsage.customer_id == customer_id
        ).order_by(desc(CustomerUsage.record_date)).limit(days)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def get_payment_history(self, customer_id: str, limit: int = 24) -> Sequence[CustomerPayment]:
        stmt = select(CustomerPayment).where(
            CustomerPayment.customer_id == customer_id
        ).order_by(desc(CustomerPayment.payment_date)).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def get_support_tickets(self, customer_id: str) -> Sequence[CustomerSupportTicket]:
        stmt = select(CustomerSupportTicket).where(
            CustomerSupportTicket.customer_id == customer_id
        ).order_by(desc(CustomerSupportTicket.created_at))
        res = await self.session.execute(stmt)
        return res.scalars().all()
