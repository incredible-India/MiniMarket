from django.shortcuts import render 
from django.utils.decorators import decorator_from_middleware 
from django.views import View
from .middleware import checkUserStatus
from django.utils.decorators import method_decorator
from marketAdmin import models as mt

# view for the newUser account creation

@checkUserStatus
def index(request):
    userdata =request.userdata
    vegitables  = mt.grocrey.objects.all()[0:12]
    grocery  = mt.vegitables.objects.all()[0:12]
    return render(request, 'index.html',{'userdata':userdata,'vegitables' :vegitables,'grocery':grocery})




