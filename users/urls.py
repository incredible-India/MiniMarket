
from django.urls import path,include
from . import views as u_view
urlpatterns = [

    path('createaccount/', u_view.index,name='home'),
    path('verify', u_view.verifyUserForm.as_view(),name='home'),
    # for the user 
   
]
