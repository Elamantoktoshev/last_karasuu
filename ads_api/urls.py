from django.contrib import admin
from django.urls import path
from ads_api.views import ads_list


urlpatterns = [
    path('list/', ads_list)
]
