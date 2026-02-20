import sqlite3

max_age = 18
min_age = 13

conn = sqlite3.connect('class.db')
cursor = conn.cursor()
sql = 'select * from student where age < ? and age >= ?'
result = cursor.execute(sql,(max_age,min_age))
result = result.fetchall()
conn.close()

print(result)
print(type(result))