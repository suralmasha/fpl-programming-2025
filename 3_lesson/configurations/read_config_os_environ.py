# pip install dotenv

import os
from dotenv import load_dotenv

load_dotenv()  # загружает .env в os.environ

"""
os.environ - встроенный словарь в Python, который содержит все переменные окружения
операционной системы для текущего процесса.
"""

DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PORT = int(os.environ.get('DB_PORT', 5432))

"""
Плюсы:
- Секреты не в коде
- Можно иметь .env.dev, .env.prod

Минусы:
- Нет строгой типизации
- Нет валидации
"""
