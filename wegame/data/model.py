from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import configparser

import os
#用os模块来读取
curpath=os.path.dirname(os.path.realpath(__file__))
cfgpath=os.path.join(curpath,"alembic.ini")

conf=configparser.ConfigParser()
conf.read(cfgpath)
url = conf.get("alembic", "sqlalchemy.url")

engine=create_engine(url, echo=False)
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


class Battle(Base):
    __tablename__ = 'battles'

    id = Column(BigInteger, primary_key=True, unique=True)
    area_id = Column(Integer)
    start_time = Column(TIMESTAMP)
    game_mode = Column(Integer)

class BattleDetail(Base):
    __tablename__ = 'battle_detail'

    id = Column(BigInteger , Sequence('battle_detail_id_seq'), primary_key=True, unique=True)
    battle_id = Column(Integer, ForeignKey("battles.id", ondelete = 'CASCADE'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete = 'CASCADE'))
    gold_left = Column(Integer)
    health = Column(Integer)
    last_round = Column(Integer)
    level = Column(Integer)
    players_eliminated = Column(Integer)
    show_last_round = Column(String(20))
    snapshot_time = Column(Integer)
    snapshot_url = Column(String(50))
    time_eliminated = Column(Text)
    total_damage_to_players = Column(Integer)
    total_trait_num = Column(Integer)
    duration = Column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint('battle_id', 'user_id'),
        {},
    )


class Chess(Base):
    __tablename__ = 'chess'

    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    tft_id = Column(Integer)
    armor = Column(String(50))
    attack = Column(String(50))
    attack_data = Column(String(50))
    attack_mag = Column(String(50))
    attack_range = Column(String(50))
    attack_speed = Column(String(50))
    crit = Column(String(50))
    display_name = Column(String(50))
    illustrate = Column(String(50))
    job_ids = Column(String(50))
    jobs = Column(String(50))
    life = Column(String(50))
    life_data = Column(String(50))
    life_mag = Column(String(50))
    magic = Column(String(50))
    name = Column(String(50))
    original_image = Column(Text)
    price = Column(String(50))
    pro_status = Column(String(50))
    race_ids = Column(String(50))
    races = Column(String(50))
    rec_equip = Column(Text)
    skill_detail = Column(Text)
    skill_image = Column(Text)
    skill_introduce = Column(Text)
    skill_name = Column(String(50))
    skill_type = Column(String(50))
    spell_block = Column(String(50))
    start_magic = Column(String(50))
    synergies = Column(String(50))
    version = Column(String(50))

    # __table_args__ = (
    #     PrimaryKeyConstraint('id', 'version'),
    #     {},
    # )


class BattleChess(Base):
    """
     需要记录比赛的版本 来对应 棋子的版本 暂未记录
    """
    __tablename__ = 'battle_chess'

    id = Column(Integer, Sequence('battle_chess_id_seq'), primary_key = True)
    battle_detail_id = Column(Integer, ForeignKey("battle_detail.id", ondelete = 'CASCADE'))
    items = Column(ARRAY(Integer))
    hero_id = Column(Integer, ForeignKey("chess.id", ondelete = 'CASCADE'))
    price = Column(Integer)
    star = Column(Integer)

