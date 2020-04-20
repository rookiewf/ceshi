from django.utils.deprecation import MiddlewareMixin


class middlewareMix(MiddlewareMixin):
    request_list = [
        '/ceshi/app/first_api'
    ]
    def process_request(self,request):
        if request.path in self.request_list:
            print('this is process_request')
        else:
            print ('this is not in process_request')
