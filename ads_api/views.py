from ads_api.models import Ads
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ads_api.serializer import AdsSerializers
# Create your views here.


@api_view(['GET'])
def ads_list(request):
    ads = Ads.objects.all()
    serializer = AdsSerializers(ads, many=True)
    return Response(serializer)


def get(self, request, format=None):
    ads = Ads.objects.all()
    serializer = AdsSerializers(ads, many=True)
    return Response(serializer.data)
