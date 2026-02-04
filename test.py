import sqlite3

conn = sqlite3.connect("restaurant.db")
cursor = conn.cursor()


conn.execute("""select * from employee""")
rows = cursor.fetchall()
for row in rows:
    print(row)



conn.close()