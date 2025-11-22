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
print(mypackage.__version__)  # если прописана переменная __version__
```

(Опционально) Установка в editable режиме
```
pip install -e .
```

(Опционально) Проверка установки
```
pip show mypackage
```
