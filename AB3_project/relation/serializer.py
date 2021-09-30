from ab3_project.team import query
from rest_framework import serializers
from .models import Relation
from ..player.serializer import Player_serializer_to_relation
from ..team import query as Team_query


class Relation_serializer(serializers.ModelSerializer):

    """
    {
        "id": x,
        "player": {
            "id": x,
            "name": "x",
            "state": "x"
        },
        "team_mate": {
            "id": x,
            "name": "x",
            "state": "x"
        },
        "points": x,
        "assists": x,
        "rebounds": x
    }
    
    """

    player = Player_serializer_to_relation()
    team_mate = Player_serializer_to_relation()

    class Meta:
        model = Relation
        fields = ['id', 'player', 'team_mate',
                  'points', 'assists', 'rebounds']


class Relation_simple_serializer(serializers.ModelSerializer):

    """
    {
        "id": x,
        "player": x,
        "team_mate": x,
        "points": x,
        "assists": x,
        "rebounds": x
    }
    
    """

    class Meta:
        model = Relation
        fields = ['id', 'player', 'team_mate', 'points', 'assists', 'rebounds']

    def validate(self, data):
        """ 
            Validamos que el compañero y el jugador no son los mismos
            y que la relacion es de jugadores del mismo equipo

        """

        if data['player'] == data['team_mate']:
            raise serializers.ValidationError(
                "El jugador y el compañero no pueden ser el mismo")
        else:
            team_team_mate = Team_query.get_from_player(data['team_mate'].id)
            team_player = Team_query.get_from_player(data['player'].id)

            if team_player != team_team_mate:
                raise serializers.ValidationError(
                    "La relación solo puede ser de jugadores del mismo equipo")

        return data
