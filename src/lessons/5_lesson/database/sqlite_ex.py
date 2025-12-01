import sqlite3

# создаем соединение с базой и файл базы данных test.db, если его нет
conn = sqlite3.connect('test.db')

# создаем объект курсора для выполнения SQL-запросов
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,  -- уникальный идентификатор
    name TEXT  -- имя пользователя
)
""")
conn.commit()  # сохраняем изменения

"""
`CREATE TABLE IF NOT EXISTS` - создаёт таблицу только если её ещё нет
`INTEGER PRIMARY KEY` - автоматически увеличивающийся `id`
`TEXT` - текстовое поле для имени
"""

# Добавление данных
cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alex',))
conn.commit()

"""
`?` - плейсхолдер для безопасной подстановки данных (защита от SQL-инъекций)
"""

# Чтение данных
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()  # возвращает все строки - список кортежей: [(1, 'Alex')]
print(rows)

# Удаление всех данных
cursor.execute('DELETE FROM users WHERE id = ?', (1,))  # удаляет только запись с указанными id - кортеж
conn.commit()

# Удаление всех данных
cursor.execute('DELETE FROM users')  # удаляем все строки
conn.commit()

conn.close()  # Важно закрывать соединение после работы с базой!
