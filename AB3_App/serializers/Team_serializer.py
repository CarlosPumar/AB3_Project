from ..models.Team import Team
from rest_framework import serializers
from .Player_serializer import Player_serializer_to_team


class Team_simple_serializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['id', 'name']


class Team_serializer(serializers.ModelSerializer):

    players = Player_serializer_to_team(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'players']
