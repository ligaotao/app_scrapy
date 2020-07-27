import redis
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
print(BASE_DIR)
from wegame.data.model import Sesssion, Battle, BattleDetail, User,update_or_create, select_or_insert, redis_password, redis_host
import datetime

class BattleReis():

  def __init__(self):
    pool = redis.ConnectionPool(host=redis_host, port=6379, password=redis_password, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    self.redis = r 
  
  def lpush(self, name, value):
    self.redis.lpush(name, value)

if __name__ == "__main__":
  session = Sesssion()
  users = session.query(User).filter(User.area_id==9).order_by(User.id)
  battle_redis = BattleReis()
  for user in users:
    battle_redis.lpush('battle_user', user.slol_id)