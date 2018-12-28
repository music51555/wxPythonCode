from django.db import models


class ListField(models.TextField):
    description = 'ListField'

    def __init__(self,*args,**kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, conn, context):
        print('from_db_value')
        if not value:
            value = []
        if isinstance(value,list):
            return value
        print('value type',type(value))

        print('value', value)

    def get_prep_value(self, value):
        print('get_prep_value')

        if not value:
            return value
        print('value type',type(value))

        return str(value)