from django.contrib import admin
from .models import Ads


class AdsAdm(admin.ModelAdmin):
    list_display = ('id', 'ad_client', 'ad_discription',
                    'ad_number', 'ad_social', 'ad_dt')
    list_display_links = ('id', 'ad_client')
    search_fields = ('ad_client', 'ad_discription',
                     'ad_number', 'ad_social', 'ad_dt')
    list_editable = ('ad_social', 'ad_number')

    # Register your models here.
admin.site.register(Ads, AdsAdm)
