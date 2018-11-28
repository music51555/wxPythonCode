from django.utils.deprecation import MiddlewareMixin

class MiddleWare_1(MiddlewareMixin):

    def process_request(self,request):
        print('MiddleWare_1 to request')

    def process_response(self,request,response):
        print('MiddleWare_1 to response')

        return response

class MiddleWare_2(MiddlewareMixin):

    def process_request(self,request):
        print('MiddleWare_2 to request')

    def process_response(self,request,response):
        print('MiddleWare_2 to response')

        return response