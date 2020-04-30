from django.http import HttpResponse

from ceshi import settings
import json


def render_json(code=0, data=None):
    result = {
        'code': code,
        'data': data
    }
    if settings.DEBUG:
        json_result = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        json_result = json.dumps(result, ensure_ascii=False, separators=(',', ':'))

    return HttpResponse(json_result)
