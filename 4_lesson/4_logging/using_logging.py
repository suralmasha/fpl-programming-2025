import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

logging.info('Запуск программы')
logging.warning('Что-то подозрительное')
logging.error('Произошла ошибка')

"""
2025-11-24 13:30:14,234 [INFO] Запуск программы
2025-11-24 13:30:14,235 [WARNING] Что-то подозрительное
2025-11-24 13:30:14,236 [ERROR] Произошла ошибка
"""
