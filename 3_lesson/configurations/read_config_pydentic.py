# pip install pydantic-settings

from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):  # для строгой типизации и валидации
    db_host: str = 'localhost'
    db_port: int = 5432
    api_key: str

    model_config = ConfigDict(env_file='.env', env_file_encoding='utf-8')


"""
Плюсы:
- Автоматическая валидация типов
- Работает с .env и переменными окружения
- Удобно для API и больших проектов
- Подходит для Dev/Test/Prod окружений
"""


if __name__ == '__main__':
    settings = Settings()
    print(settings.db_host, settings.db_port, settings.api_key)
