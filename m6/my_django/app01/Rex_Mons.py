class Mons:
    regex = '[0-9]{2}'

    def to_python(self,value):
        return int(value)

    #用于反向解析
    def to_url(self,value):
        return '%04d' % value