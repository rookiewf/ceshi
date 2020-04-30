import requests
from ceshi import cfg


def get_access_token(code):
    WB_ACCESS_ARGS = cfg.WB_ACCESS_ARGS.copy()
    WB_ACCESS_ARGS['code'] = code
    response = requests.post(url=cfg.WB_ACCESS_API, data=WB_ACCESS_ARGS)
    if response.status_code == 200:
        result = response.json()
        access_token = result['access_token']
        uid = result['uid']
        return access_token, uid
    else:
        return None, None


def get_user_info(access_token, uid):
    WB_USER_SHOW_ARGS = cfg.WB_USER_SHOW_ARGS.copy()
    WB_USER_SHOW_ARGS['access_token'] = access_token
    WB_USER_SHOW_ARGS['uid'] = uid
    response = requests.get(url=cfg.WB_USER_SHOW_API, params=WB_USER_SHOW_ARGS)
    if response.status_code == 200:
        result = response.json()
        user_info = {
            'name': result['name'],
            'sex': 'fmale' if result['gender'] == 'f' else 'male',
        }
        return user_info
    return None
