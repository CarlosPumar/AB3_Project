from .models import Player
from rest_framework import serializers


class Player_serializer_to_relation(serializers.ModelSerializer):

    """
    {
        "id": x,
        "name": "x",
        "state": "x"
    }

    """

    class Meta:
        model = Player
        fields = ['id', 'name', 'state']


class Player_simple_serializer(serializers.ModelSerializer):

    """
    {
        "id": x,
        "name": "x",
        "state": "x",
        "team": x
    }

    """

    class Meta:
        model = Player
        fields = ['id', 'name', 'state', 'team']
