from django.contrib import admin

from .models import Vendor, Consumer


@admin.register(Vendor)
class data(admin.ModelAdmin):
    list_display  = ['id','name','email','created']


@admin.register(Consumer)
class data(admin.ModelAdmin):
    list_display  = ['id','name','email','created']

