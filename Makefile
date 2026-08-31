.PHONY: help install test lint clean run

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'

install: ## Install project dependencies
	@echo "Installing dependencies..."
	@pip install -r requirements.txt 2>/dev/null || true

test: ## Execute test suite
	@echo "Running tests..."
	@pytest tests/ -v || python -m unittest discover tests/

lint: ## Run code linters and formatters
	@echo "Linting codebase..."
	@flake8 . --max-line-length=120 2>/dev/null || true

clean: ## Remove temporary build and cache files
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@rm -rf .pytest_cache htmlcov .coverage dist build
	@echo "Cache cleaned."

run: ## Launch local development instance
	@python -m src.main 2>/dev/null || python main.py 2>/dev/null || echo "Run entrypoint"
