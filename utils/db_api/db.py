import asyncio


from sqlalchemy import create_engine
from sqlalchemy import and_
from sqlalchemy import Column, Integer,String, ForeignKey

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()

class Note(Base):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer)
    header = Column(String)
    text = Column(String)
    time = Column(String)

    def __init__(self, uid, header,text,time):
        self.uid = uid
        self.header = header
        self.text = text
        self.time = time


engine = create_engine('sqlite:///.\db.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def create_db():
    Base.metadata.create_all(engine)

def add_note(uid,header,text,time='now'):
    querry = Note(uid,header,text,time)
    session.add(querry)
    session.commit()

def get_notes(uid):
    querry = session.query(Note).filter(Note.uid==uid).all()
    if querry:
        text = 'Ваши заметки\n'
        for row in querry:
            text = text + f'''
                       <b>{row.header}</b>

            <i>{row.text}</i>

            {row.time}          /del{row.id}
            '''
    else:
        text = 'Не заведено ни одной заметки'
    return text

def del_note(uid,id):
    obj = session.query(Note).filter(and_(Note.id==id,Note.uid==uid)).one()
    session.delete(obj)
    session.commit()


def get_all_data():
    querry = session.query(Note).all()
    return querry


