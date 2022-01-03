
from django.urls import path,include
from . import views as u_view
urlpatterns = [

    path('createaccount/', u_view.index,name='home'),
    path('login/', u_view.loginForm.as_view(),name='login'),
    path('verify', u_view.verifyUserForm.as_view(),name='home'),
    path('logout/', u_view.userLogout.as_view(),name='logout'),
    path('mycart/<int:id>/<int:price>/<str:name>/', u_view.AddtoCart.as_view(),name='cart'),
    path('show/mycart/', u_view.mycart,name='mycart'),
    path('deleteitem/<int:id>/', u_view.deleteFromCart,name='dmycart'),
    path('delete/all/', u_view.deleteAllFRMCART,name='damycart'),
    path('buy/all/<int:totalAm>/<int:totalIt>/', u_view.BuyFRMCart,name='damycart'),
    path('confirmBuy/', u_view.CnfBuyFRMCart,name='damycart'),
    path('buysingle/<int:id>/veg/', u_view.DRCTBuyFrmcrd,name='damaycart'),
    path('buysingle/<int:id>/groc/', u_view.DRCTBuyFrmcrdGroce,name='damaycart'),
    path('confirm/buy/', u_view.confirmBuy,name='damaycart'),
    # for the user 
   
]
