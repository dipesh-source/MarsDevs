from django.contrib import admin

from .models import Vendor, Consumer, Movies, Viewers


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


# have a tabular inline
class moviesData(admin.TabularInline):
    model = Viewers

@admin.register(Movies)
class Movies_admin(admin.ModelAdmin):
    inlines = [moviesData]
    list_display  = ['id','name','hero','types','created']
    list_filter = ['name','hero','types','created']
    search_fields = ['name','hero','types']
    list_editable = ['name','hero']
    ordering = ['name']
    readonly_fields = ['created']
    list_per_page = 10


@admin.register(Viewers)
class Viewers_admin(admin.ModelAdmin):
    list_display  = ['id','movies','vname','age','city','created']
    autocomplete_fields = ['movies']
    list_filter = ['vname','age','city','created']
    search_fields = ['vname','age','city']
    list_editable = ['vname','city']
    ordering = ['vname']
    readonly_fields = ['created']
    list_per_page = 10