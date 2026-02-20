import sqlite3

conn = sqlite3.connect('class.db')
cursor = conn.cursor()
sql = 'select * from student'
result = cursor.execute(sql,)
result = result.fetchall()
conn.close()

print(result)

for x in result:
    print(x)

for x in result:
    print(f'{x[1]} \t {x[2]}')