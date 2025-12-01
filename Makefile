init:
	poetry install & \
	poetry run pre-commit install

update:
	poetry update

build:
	poetry build

ruff:
	poetry run ruff check
ruff-fix:
	poetry run ruff check --fix
ruff-unsafe-fix:
	poetry run ruff check --fix --unsafe-fixes
ruff-format:
	poetry run ruff format
