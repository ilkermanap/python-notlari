from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from sqlite_sqlalchemy_ex import Kisi, Base, Adres
 
engine = create_engine('sqlite:///sqlalchemy_ornek.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
 
# Kisi tablosuna kayit girelim
yeni_kisi = Kisi(adi='Yeni Kisi')
session.add(yeni_kisi)
session.commit()
 
# Adres tablosuna kayit girelim
yeni_adres = Adres(posta_kodu='00000', kisi=yeni_kisi)
session.add(yeni_adres)
session.commit()
