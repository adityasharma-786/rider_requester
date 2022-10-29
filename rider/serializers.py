from rest_framework import serializers
from rider.models import *

class RequesterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requester
        fields = "__all__"

class RiderDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = "__all__"