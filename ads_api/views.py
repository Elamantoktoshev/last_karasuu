from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *


class AdsApiView(APIView):
    serializer_class = AdsSerializers

    def get(self, request):
        AllAds = Ads.objects.all().values()
        return Response({"message": "List of Ads", "Ads list": AllAds})

    def post(self, request):
        print("REquest date is: ", request.data)
        serializer_obj = AdsSerializers(data=request.data)
        if (serializer_obj.is_valid()):

            Ads.objects.create(id=serializer_obj.data.get("id"),
                               name=serializer_obj.data.get("name"),
                               image=serializer_obj.data.get("image"),
                               discription=serializer_obj.data.get(
                                   "discription"),
                               number=serializer_obj.data.get("number"),
                               social=serializer_obj.data.get("social"),
                               dt=serializer_obj.data.get("Date"),
                               )

        ad = Ads.objects.all().filter(id=request.data["id"]).values()
        return Response({"message": "New ad added", "Ads": ad})
