from multiprocessing import cpu_count
bind = '127.0.0.1:9000'
daemon = True
workers = cpu_count()*2
# worker_class = 'gevent' # 指定异步处理的库
worker_class = 'egg:meinheld#gunicorn_worker'
worker_connections = 65535
keepalive = 60
timeout = 30
graceful_timeout = 10
frowarded_allow_ips = '*'
capture_output=True
loglevel='info'
errorlog='logs/error.logs'

# import multiprocessing
#
# bind = '127.0.0.1:8000'
# workers = multiprocessing.cpu_count() * 2 + 1
#
# backlog = 2048
# worker_class = "gevent"
# worker_connections = 1000
# daemon = False
# debug = True
# proc_name = 'gunicorn_demo'
# pidfile = './logs/gunicorn.pid'
# errorlog = './logs/gunicorn.logs'