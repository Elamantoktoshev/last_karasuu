from django.contrib import admin
from .models import Ads


class AdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'discription',
                    'number', 'social', 'dt')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'discription',
                     'number', 'social', 'dt')
    list_editable = ('social', 'number')


class BookAmd(admin.ModelAdmin):
    list_display = ('title')
    list_display_links = ('id', 'title')
    list_editable = ('title')


# Register your models here.
admin.site.register(Ads, AdsAdmin)
