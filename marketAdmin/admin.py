from django.contrib import admin
from .models import grocrey,vegitables



# Register your models here.
@admin.register(grocrey)
class grocreyAdmin(admin.ModelAdmin):
    list_display = ['id','gname','gprice','ginfo','gamm','gimg']


@admin.register(vegitables)
class vegitablesAdmin(admin.ModelAdmin):
    list_display = ['id','vname','vprice','vinfo','vamm','vimg']