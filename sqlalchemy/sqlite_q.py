import sqlite3
conn = sqlite3.connect('ornek.db')
 
c = conn.cursor()
c.execute('SELECT * FROM kisi')
print(c.fetchall())
c.execute('SELECT * FROM adres')
print(c.fetchall())
conn.close()
