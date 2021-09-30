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


class Player_serializer(serializers.ModelSerializer):

    """
    {
        "id": x,
        "name": "x",
        "state": "x",
        "team": {
            "id": x,
            "name": "x"
        },
        "relation": [
            {
                "id": x,
                "player": x,
                "team_mate": x,
                "points": x,
                "assists": x,
                "rebounds": x
            }
        ]
    }

    """

    # Importamos aqui para no tener errores de importaciones circulares
    from ..team.serializer import Team_simple_serializer
    from ..relation.serializer import Relation_simple_serializer

    team = Team_simple_serializer()
    relation = Relation_simple_serializer(read_only=True, many=True)

    class Meta:
        model = Player
        fields = ['id', 'name', 'state', 'team', 'relation']