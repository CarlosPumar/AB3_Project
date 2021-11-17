from rest_framework import serializers
from .models import Player

# This file is create to avoid cycle import errors


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

    from ..team.serializer import Team_simple_serializer
    from ..relation.serializer import Relation_serializer_to_player

    team = Team_simple_serializer()
    relation = Relation_serializer_to_player(read_only=True, many=True)

    class Meta:

        model = Player
        fields = ['id', 'name', 'state', 'team', 'relation']
