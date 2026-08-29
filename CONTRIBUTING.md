# Contributing Guidelines

Thank you for contributing to the platform! Please review our guidelines below before submitting pull requests.

## Development Workflow
1. Fork and clone the repository.
2. Create a focused feature branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Implement your changes adhering to clean architecture principles.
4. Add corresponding unit and integration tests under `tests/`.
5. Run the test suite and linters to verify zero regressions.
6. Commit using standard Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`).
7. Push your branch and open a Pull Request.

## Code Standards
- Adhere strictly to PEP 8 / clean code conventions.
- Maintain type hints across all service interfaces and business logic.
- Ensure thorough docstrings explaining domain invariants and algorithmic complexity.
