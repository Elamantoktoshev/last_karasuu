# from ads_api.models import Ads
# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from ads_api.serializer import AdsSerializers
# # Create your views here.


# @api_view(['GET'])
# def ads_list(request):
#     ads = Ads.objects.all()
#     serializer = AdsSerializers(ads, many=True)
#     return Response(serializer)


# def get(self, request, format=None):
#     ads = Ads.objects.all()
#     serializer = AdsSerializers(ads, many=True)
#     return Response(serializer.data)


from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *


class AdsApiView(APIView):
    serializer_class = AdsSerializers

    def get(self, reguest):
        allAds = AdsKarasuu.objects.all().values()
        return Response({'massage': 'List of ads', 'ads list': allAds})

    def post(self, request):
        print('request date is: ', request.data)
        serializer_obj = AdsSerializers(data=request.data)
        if (serializer_obj.is_valid()):

            AdsKarasuu.objects.create(
                id=serializer_obj.data.get("id"),
                # ad_image=serializer_obj.data.get("фото"),
                client_name=serializer_obj.data.get("Имя клиента"),
                discription=serializer_obj.data.get("Описание"),
                number=serializer_obj.data.get("Номер клиента"),
                social=serializer_obj.data.get("Соц. сет клиента"),
                dt=serializer_obj.data.get("Дата"),
            )

        ad = AdsKarasuu.objects.all().filter(id=request.data["id"]).values()
        return Response({'massage': 'New ad added', 'ad list': ad})
