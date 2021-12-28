from django.contrib import admin
from .models import Users,cart
# Register your models here.
@admin.register(Users)
class UsersModel(admin.ModelAdmin):
    list_display = ['name','password','email','mobile','address','id']

@admin.register(cart)
class UsersModel(admin.ModelAdmin):
    list_display = ['uid','item_price','item_name','id',]