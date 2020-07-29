import redis
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
import json
from sqlalchemy import between

from wegame.data.model import Sesssion, Battle, BattleDetail, User,update_or_create, select_or_insert, redis_password, redis_host
import datetime

class BattleReis():

  def __init__(self):
    pool = redis.ConnectionPool(host=redis_host, port=6379, password=redis_password, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    self.redis = r 
  
  def lpush(self, name, value):
    self.redis.lpush(name, value)
  
  def clear(self, name):
    self.redis.delete(name)

if __name__ == "__main__":
  session = Sesssion()
  battle_redis = BattleReis()
  battle_redis.clear('battle_user')

  users = session.query(User).filter(User.area_id != None).filter(between(User.ranking, 0, 20)).order_by(User.id)
  
  for user in users:
    user_obj = { "slol_id": user.slol_id, "area_id": user.area_id}
    battle_redis.lpush('battle_user', json.dumps(user_obj, ensure_ascii=False))