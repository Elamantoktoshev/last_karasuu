from django.contrib.auth.models import User, Group
from rest_framework import serializers


class AdsSerializers(serializers.Serializer):
    id = serializers.IntegerField(label="id")
    # title = serializers.CharField(label="title")
    # author = serializers.CharField(label="author")
    ad_image = serializers.ImageField(label="Фото")
    client_name = serializers.CharField(label="Имя клиента")
    discription = serializers.CharField(label="Описания")
    number = serializers.CharField(label="Номер клиент")
    social = serializers.CharField(label="Соц. сет")
    dt = serializers.DateTimeField(label="Дата")
