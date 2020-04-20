from ceshi.cfg import REDIS_ARGS
import redis
rds = redis.StrictRedis(**REDIS_ARGS,decode_responses=True)

