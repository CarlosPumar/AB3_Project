from rest_framework import serializers
from .models import Team


class Team_simple_serializer(serializers.ModelSerializer):

    """
    {
        "id": x,
        "name": "x"
    }
    """

    class Meta:

        model = Team
        fields = ['id', 'name']


class Team_serializer(serializers.ModelSerializer):

    from ..player.serializer import Player_serializer_to_relation
    players = Player_serializer_to_relation(many=True, read_only=True)

    class Meta:

        players = []

        model = Team
        fields = ['id', 'name', 'players']
