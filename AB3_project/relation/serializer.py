from rest_framework import serializers
from .models import Relation


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
    from ..player.serializer import Player_serializer_to_relation

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

        from ..team.models import Team

        if data['player'] == data['team_mate']:
            raise serializers.ValidationError(
                "El jugador y el compañero no pueden ser el mismo")
        else:
            team_team_mate = Team.objects.get(pk=data['team_mate'].team.id)
            team_player = Team.objects.get(pk=data['player'].team.id)

            if team_player != team_team_mate:
                raise serializers.ValidationError(
                    "La relación solo puede ser de jugadores del mismo equipo")

        return data


class Relation_serializer_to_player(serializers.ModelSerializer):

    """
        {
        "id": x,
        "player": x,
        "team_mate": {
            "id": x
            "name": "x"
        },
        "points": x,
        "assists": x,
        "rebounds": x
    }
    """
    from ..player.serializer import Player_serializer_to_relation
    team_mate = Player_serializer_to_relation()

    class Meta:
        model = Relation
        fields = ['id', 'player', 'team_mate', 'points', 'assists', 'rebounds']
