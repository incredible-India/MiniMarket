from django.shortcuts import render 
from django.utils.decorators import decorator_from_middleware 
from django.views import View
from .middleware import checkUserStatus
from django.utils.decorators import method_decorator
# view for the newUser account creation

@checkUserStatus
def index(request):
    userdata =request.userdata
    return render(request, 'index.html',{'userdata':userdata})




