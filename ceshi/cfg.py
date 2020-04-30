import urllib.parse

QNY = 'rookiewf'
REDIS_ARGS = dict(
    host='localhost',
    port=6379,
    password='123456',
    db=1,
    decode_responses=True
)

# 微博登录接入
# 1. 微博回调页
AUTHAPI = 'https://api.weibo.com/oauth2/authorize'
APPKEY = '1274254980'
APPSECRET = '56f3e5d160f68f2d65a62ccc721e9b61'
CALLBACK = 'http://127.0.0.1:8000/ceshi/app/wb_callback'
AUTHORIZA_ARGS = {
    'client_id': APPKEY,
    'redirect_uri': CALLBACK,
    'display': 'default'
}
WB_AUTH_URL = '%s?%s' % (AUTHAPI, urllib.parse.urlencode(AUTHORIZA_ARGS))
# 2. accesstoken 接口
WB_ACCESS_API = 'https://api.weibo.com/oauth2/access_token'
WB_ACCESS_ARGS = {
    'client_id': APPKEY,
    'client_secret': APPSECRET,
    'grant_type': 'authorization_code',
    'code': None,
    'redirect_uri': CALLBACK
}
# 3. 获取用户信息
WB_USER_SHOW_API = 'https://api.weibo.com/2/users/show.json'
WB_USER_SHOW_ARGS = {
    'access_token': None,
    'uid': None
}
import datetime

# 支付宝 支付
# TODO eg:'https://openapi.alipay.com/gateway.do?
#  timestamp=2013-01-01 08:08:08
#  &method=alipay.trade.app.pay&app_id=17063
#  &sign_type=RSA2&
#  sign=ERITJKEIJKJHKKKKKKKHJEREEEEEEEEEEE&version=1.0
#  &charset=GBK&biz_content='
ALIPAN_API = 'https://openapi.alipay.com/gateway.do'
APP_ID = '2021001159697269'
ALIPAN_ARGS = {
    'app_id': ALIPAN_API,
    'method': 'alipay.trade.wap.pay',
    'charset': 'utf-8',
    'sign_type': 'RSA2',
    'sign': '',
    'timestamp': (datetime.datetime.today()).strftime('%Y-%m-%d %H:%M:%S'),
    'version': '1.0',
    'biz_content': '',
}
