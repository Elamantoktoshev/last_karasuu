from rest_framework import serializers


class AdsSerializers(serializers.Serializer):
    id = serializers.IntegerField(label="id")
    name = serializers.CharField(label=" client name")
    image = serializers.ImageField(label="Image")
    discription = serializers.CharField(label="discriptions")
    number = serializers.CharField(label="Number")
    social = serializers.CharField(label="social")
    dt = serializers.DateTimeField(label="date time")
