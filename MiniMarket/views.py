from django.shortcuts import render 
from django.utils.decorators import decorator_from_middleware 
from django.views import View
# view for the newUser account creation

def index(request):
    return render(request, 'index.html')




