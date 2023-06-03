.PHONY: test
test:
	pytest tests/ -v --cov=app --cov-report=html --cov-fail-under=100 tests