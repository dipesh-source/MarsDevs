from django.contrib import admin

from .models import Vendor, Consumer


# class ConsumerTab(admin.StackedInline):
#     model = Consumer

class ConsumerTab(admin.TabularInline):
    model = Consumer


@admin.register(Vendor)
class Vendor_admin(admin.ModelAdmin):
    inlines = (ConsumerTab,)
    # list_display  = ['id','name','email','created']
    list_display = ('id', 'name', 'email', 'created')
    search_fields = ['name','email']
    list_filter = ['name', 'email']
    list_editable = ['name','email']
    ordering = ['name']
    readonly_fields = ['created']
    #pagination
    list_per_page = 10

@admin.register(Consumer)
class Consumer_admin(admin.ModelAdmin):
    list_display  = ['id','vendor','name','email','age','created']
    autocomplete_fields = ['vendor']
    list_filter = ['name','email','age','created']
    search_fields = ['name','email','age']
    list_editable = ['email','age']
    ordering = ['email']
    readonly_fields = ['created']
    list_per_page = 10
