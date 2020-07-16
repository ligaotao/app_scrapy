from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.orm import sessionmaker
import configparser

import os
#用os模块来读取
curpath=os.path.dirname(os.path.realpath(__file__))
cfgpath=os.path.join(curpath,"alembic.ini")

conf=configparser.ConfigParser()
conf.read(cfgpath)
url = conf.get("alembic", "sqlalchemy.url")

engine=create_engine(url)
Sesssion=sessionmaker(bind=engine)
# session=Sesssion()

Base = declarative_base()
metadata = Base.metadata

def update_or_create(session, model, **kwargs):
    created = False

    defaults = kwargs['defaults']
    select_dict = kwargs.pop('defaults', {})
    obj = session.query(model).filter_by(**select_dict).first()
    if obj is not None:
        for k, v in defaults.items():
            setattr(obj, k, v() if callable(v) else v)
    else:
        kwargs.update(defaults)
        obj = model(**kwargs)
        session.add(obj)
        created = True
    session.commit()
    return obj, created

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    slol_id = Column(String(50))
    name = Column(String(50))
    level = Column(Integer)
    ranking = Column(Integer)
    league_points = Column(Integer)
    rank = Column(Integer)
    icon_id = Column(Integer)
    tier = Column(Integer)
    area_id = Column(Integer)

    def __repr__(self):
        return "<User (name='%s')>" (self.name)
