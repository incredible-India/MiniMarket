from types import NoneType
from django.shortcuts import HttpResponseRedirect

class userAuthentication:

    def __init__(self,get_response):
        self.get_response  =get_response
    
    def __call__(self,request):
        if 'name' in request.session:
            print(request.session['name'])
            if 'email' in request.session:
                print(request.session['email'])
                return HttpResponseRedirect('/')
        
        response = self.get_response(request)
        return response



