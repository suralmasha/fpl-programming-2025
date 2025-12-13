Для сборки пакета необходимо собрать пакет в дистрибутив:
```shell
python setup.py sdist bdist_wheel
```

или

```shell
python -m build
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
pip install --force-reinstall dist/mypackage-0.1.0-py3-none-any.whl
```

После этого пакет будет доступен в Python:

```python
import mypackage
```

(Опционально) Установка в editable режиме
```
pip install -e .
```

(Опционально) Проверка установки
```
pip show mypackage
```

# Публикация пакета на PyPI

Ниже приведены способы публикации Python-пакета на PyPI.

## Установите необходимые инструменты
```
pip install --upgrade build twine
```

- `build` — для сборки дистрибутива пакета.
- `twine` — для безопасной загрузки пакета на PyPI.

## Проверьте пакет (опционально)

Вы можете проверить пакет перед публикацией на тестовом PyPI:

```
twine check dist/*
```

## Загрузите пакет на PyPI

### На тестовый PyPI (рекомендуется сначала проверять):
```
twine upload --repository testpypi dist/*
```
Потребуется создать учетную запись на https://test.pypi.org.


### На основной PyPI (после проверки):
```
twine upload dist/*
```
Потребуется учетная запись на https://pypi.org.

После этого ваш пакет доступен для всех пользователей PyPI.

## Установка опубликованного пакета

После успешной публикации его можно установить через pip:

### с основного PyPI
```
pip install mypackage
```

### или с тестового PyPI
```
pip install --index-url https://test.pypi.org/simple/ mypackage
```
