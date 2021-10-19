import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Kisi(Base):
    __tablename__ = 'kisi'
    # Burada kisi tablosu icin alanları tanimliyoruz.
    id = Column(Integer, primary_key=True)
    adi = Column(String(250), nullable=False)
 
class Adres(Base):
    __tablename__ = 'adres'
    # Burada adres tablosu icin alanları tanimliyoruz.
    id = Column(Integer, primary_key=True)
    mahalle = Column(String(250))
    sokak = Column(String(250))
    posta_kodu = Column(String(250), nullable=False)
    kisi_id = Column(Integer, ForeignKey('kisi.id'))
    kisi = relationship(Kisi)

    

# Bulundugumuz dizinde sqlalchemy_ornek.db dosyasi yaratacak olan
# veritabani motorunu olustur.
engine = create_engine('sqlite:///sqlalchemy_ornek.db')

# Motoru kullanarak tablolari yarat. 
Base.metadata.create_all(engine)
