# Создаём проект

```
mkdir myproject
cd myproject
poetry init
```

`poetry init` задаст вопросы:
- название проекта
- версию
- описание
- author
- лицензия
- зависимости
(можно пропустить, потом добавим)

В итоге создастся `pyproject.toml`

# Устанавливаем зависимости

Продакшн-зависимости:

```
poetry add requests
poetry add fastapi
```

Dev-зависимости - эти пакеты нужны только для разработки / тестов / линтера

```
poetry add --dev pytest mypy ruff
```

Это автоматически обновит `pyproject.toml`
Создаст lock-файл `poetry.lock` с зафиксированными версиями

# Активируем виртуальное окружение

```
poetry shell
```

`deactivate` - выйти из окружения

# Запуск тестов и линтера

```
# Запустить тесты
poetry run pytest

# Проверить типы
poetry run mypy src/

# Проверить стиль кода
poetry run ruff check src/
```