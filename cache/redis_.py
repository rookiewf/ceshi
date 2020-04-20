from ceshi.cfg import REDIS_ARGS
import redis
rds = redis.Redis(**REDIS_ARGS)
