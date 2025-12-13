# pip install structlog / poetry add structlog
import sys

import structlog

# Настройка structlog
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt='iso'),  # Добавляет временную метку к каждому событию
        structlog.processors.add_log_level,  # Добавляет уровень лога (info, warning, error) к каждому событию
        structlog.processors.KeyValueRenderer(key_order=['timestamp', 'level', 'event']),
        # Форматирует вывод в удобный для чтения key=value вид
    ],
    logger_factory=structlog.PrintLoggerFactory(file=sys.stdout),
    # Определяем, куда будут выводиться логи - в stdout (либо можно в файл.json)
)

logger = structlog.get_logger()

# Пример логов
logger.info('Запуск программы')
logger.warning('Что-то подозрительное', user='my_user')
logger.error('Произошла ошибка', code=500)

"""
timestamp='2025-11-22T17:05:01.123456' level='info' event='Запуск программы'
timestamp='2025-11-22T17:05:01.123789' level='warning' event='Что-то подозрительное' user='my_user'
timestamp='2025-11-22T17:05:01.124012' level='error' event='Произошла ошибка' code=500
"""
