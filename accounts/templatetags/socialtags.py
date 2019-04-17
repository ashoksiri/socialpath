import json


from django import template
from django.forms import model_to_dict
from django.utils.safestring import mark_safe
from datetime import datetime

class DataEncoder(json.JSONEncoder):

    def default(self, o):

        if isinstance(o,datetime):
            return o.__str__()
        return str(o)

register = template.Library()

@register.filter
def jsonify(object):
    return mark_safe(json.dumps(model_to_dict(object), cls=DataEncoder))

jsonify.is_safe = True