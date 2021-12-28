
from django.urls import path
from . import views as p_view
urlpatterns = [

  
    # for the user 
    path('vegs/',p_view.VegitableList.as_view(),name='vegs'),
    path('groc/',p_view.GroceryList.as_view(),name='groce')
]
