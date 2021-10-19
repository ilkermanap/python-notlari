import sqlite3
conn = sqlite3.connect('ornek.db')
 
c = conn.cursor()
c.execute('''
          CREATE TABLE kisi
          (id INTEGER PRIMARY KEY ASC, adi varchar(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE adres
          (id INTEGER PRIMARY KEY ASC, mahalle varchar(250), sokak varchar(250),
           posta_kodu varchar(250) NOT NULL, kisi_id INTEGER NOT NULL,
           FOREIGN KEY(kisi_id) REFERENCES kisi(id))
          ''')
 
c.execute('''
          INSERT INTO kisi VALUES(1, 'Ilker Manap')
          ''')
c.execute('''
          INSERT INTO adres VALUES(1, 'Stokholm', '1', '00000', 1)
          ''')
 
conn.commit()
conn.close()
