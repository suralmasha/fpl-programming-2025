Для сборки пакета необходимо собрать пакет в дистрибутив:
```shell
poetry build
```

После этого появятся файлы:
```
dist/
    mypackage-0.1.0-py3-none-any.whl
    mypackage-0.1.0.tar.gz
```

.whl — колесо, бинарный дистрибутив, быстрее ставится.
.tar.gz — исходный дистрибутив, можно использовать на любой системе с Python.

Установка пакета:
```shell
pip install dist/mypackage-0.1.0-py3-none-any.whl
```

или

```shell
poetry add dist/mypackage-0.1.0-py3-none-any.whl
```

После этого пакет будет доступен в Python:

```python
import mypackage
```

# Публикация пакета на PyPI

Ниже приведены способы публикации Python-пакета на PyPI.

Никакие дополнительные инструменты не нужны

## Загрузите пакет на PyPI

```
poetry publish dist/*
```
Потребуется учетная запись на https://pypi.org.

После этого ваш пакет доступен для всех пользователей PyPI.

## Установка опубликованного пакета

После успешной публикации его можно установить через pip:
```
pip install mypackage
```

или poetry
```
poetry add mypackage
```
