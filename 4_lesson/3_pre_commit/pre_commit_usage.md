Необходимо добавить `pre-commit` в зависимости (в `dev` зависимости, если используете Poetry).

В корне создать файл `.pre-commit-config.yaml`.

Для подкдючения пре-коммита нужно выполнить в корне команду
```
pre-commit install
```

или (если используете Poetry)
```
poetry pre-commit install
```

Пре-коммит будет запускаться перед каждым коммитом.


Отключить пре-коммит для всего проекта:
```
pre-commit uninstall
```

или (если используете Poetry)
```
poetry pre-commit uninstall
```