from ..models.Player import Player
from rest_framework import serializers


class Player_serializer_to_team(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ['id', 'name', 'state']


class Player_simple_serializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ['id', 'name', 'state', 'team']


class Player_serializer(serializers.ModelSerializer):

    # Importamos aqui para no tener errores de importaciones circulares
    from .Team_serializer import Team_simple_serializer
    from .Relation_serializer import Relation_simple_serializer

    team = Team_simple_serializer()
    relation = Relation_simple_serializer(read_only=True, many=True)

    class Meta:
        model = Player
        fields = ['id', 'name', 'state', 'team', 'relation']
