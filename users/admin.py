from django.contrib import admin
from .models import Users
# Register your models here.
@admin.register(Users)
class UsersModel(admin.ModelAdmin):
    list_display = ['name','password','email','mobile','id']