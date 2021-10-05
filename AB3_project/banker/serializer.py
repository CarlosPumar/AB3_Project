from .models import Banker
from rest_framework import serializers


class Banker_serializer(serializers.ModelSerializer):

    class Meta:
        model = Banker
        fields = ['id', 'text']
