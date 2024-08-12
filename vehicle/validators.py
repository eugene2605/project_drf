import re
from rest_framework.serializers import ValidationError


class TitleValidator:

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        reg = re.compile('^[0-9a-zA-Z\.\-\ ]+$')
        tmp_val = dict(value).get(self.fields)
        if not bool(reg.match(tmp_val)):
            raise ValidationError('Title is not OK')
