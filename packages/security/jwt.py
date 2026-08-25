"""JWT access and refresh token generation, verification, and rotation."""

import datetime
from typing import Dict, Any, Optional
from jose import jwt, JWTError
from packages.configuration.settings import settings
from packages.core.exceptions import AuthenticationError

class JwtTokenManager:
    @staticmethod
    def create_access_token(subject: str, roles: list[str], permissions: list[str], extra_claims: Optional[Dict[str, Any]] = None) -> str:
        now = datetime.datetime.utcnow()
        expire = now + datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        
        claims: Dict[str, Any] = {
            "sub": subject,
            "roles": roles,
            "permissions": permissions,
            "iat": now,
            "exp": expire,
            "type": "access",
        }
        if extra_claims:
            claims.update(extra_claims)
            
        return jwt.encode(claims, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    @staticmethod
    def create_refresh_token(subject: str) -> str:
        now = datetime.datetime.utcnow()
        expire = now + datetime.timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        
        claims: Dict[str, Any] = {
            "sub": subject,
            "iat": now,
            "exp": expire,
            "type": "refresh",
        }
        return jwt.encode(claims, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    @staticmethod
    def decode_token(token: str) -> Dict[str, Any]:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            return payload
        except JWTError as e:
            raise AuthenticationError(f"Invalid or expired token: {str(e)}")
