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

CAT_URL = https://cataas.com/cat/says/Write%20better%20code%20please
cat:
	@python3 -c "import webbrowser; webbrowser.open('$(CAT_URL)')"


# ASCII-баннер (рисунок, оформленный текстовыми символами ASCII - английские буквы, цифры, знаки препинания)
banner:
	pyfiglet "Write Better Code!"

