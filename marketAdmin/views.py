from django.http import request
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .models import vegitables,grocrey
from django.utils.decorators import method_decorator
from MiniMarket.middleware import checkUserStatus
# Create your views here.


# grocery wala hai
# @method_decorator(checkUserStatus)

class VegitableList(ListView):
  
    model = vegitables
    
    template_name = 'marketAdmin/vegitables.html'
    context_object_name = 'grocery'
    ordering = ['id']
    paginate_by = 7



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["userdata"] =  self.request.userdata
        return context

   



 
    
  

   


#   sabji wala hai   
class GroceryList(ListView):
    model = grocrey
    template_name = 'marketAdmin/groce.html'
    context_object_name = 'vegitables'
    ordering = ['id']
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["userdata"] =  self.request.userdata
        return context

    