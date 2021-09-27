from ..models.Team import Team
from rest_framework import serializers


class Team_simple_serializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['id', 'name']


class Team_serializer(serializers.ModelSerializer):

    # Importamos aqui para no tener errores de importaciones circulares
    from .Player_serializer import Player_serializer_to_team

    players = Player_serializer_to_team(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'players']
