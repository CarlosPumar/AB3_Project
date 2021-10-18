from .models import Player
from ..team.models import Team
from ..relation.models import Relation
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
            fields = ['id', 'player', 'team_mate',
                      'points', 'assists', 'rebounds']

        def validate(self, data):
            """ 
                Validamos que el compañero y el jugador no son los mismos
                y que la relacion es de jugadores del mismo equipo

            """

            from ..team.models import Team

            if data['player'] == data['team_mate']:
                raise serializers.ValidationError(
                    "El jugador y el compañero no pueden ser el mismo")
            else:
                team_team_mate = Team.objects.get(pk=data['team_mate'].id)
                team_player = Team.objects.get(pk=data['player'].id)

                if team_player != team_team_mate:
                    raise serializers.ValidationError(
                        "La relación solo puede ser de jugadores del mismo equipo")

            return data

    team = Team_simple_serializer()
    relation = Relation_simple_serializer(read_only=True, many=True)

    class Meta:
        model = Player
        fields = ['id', 'name', 'state', 'team', 'relation']
