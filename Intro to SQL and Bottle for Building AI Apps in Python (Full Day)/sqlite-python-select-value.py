import sqlite3

age = 13

conn = sqlite3.connect('class.db')
cursor = conn.cursor()
sql = 'select * from student where age < ?'
result = cursor.execute(sql,(age,))
result = result.fetchall()
conn.close()

print(result)