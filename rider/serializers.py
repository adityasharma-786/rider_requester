from rest_framework import serializers
from rider.models import *

class RequesterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requester
        fields = "__all__"