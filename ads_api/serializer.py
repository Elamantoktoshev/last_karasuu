from django.contrib.auth.models import User, Group
from rest_framework import serializers


class AdsSerializers(serializers.Serializer):
    ad_image = serializers.ImageField()
    ad_client = serializers.CharField()
    ad_discription = serializers.CharField()
    ad_number = serializers.CharField()
    ad_social = serializers.CharField()
    ad_dt = serializers.DateTimeField()
