import json

from django.conf import settings
from django.http import HttpResponse


def render_json(code=0, data=None):
    result = {
        'code': code,
        'data': data
    }
    if settings.DEBUG:
        json_result = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=4)
    else:
        json_result = json.dumps(result, ensure_ascii=False, separators=(',', ':'))
    return HttpResponse(json_result)
