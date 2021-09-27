from rest_framework import serializers
from ..models.Relation import Relation
from ..serializers.Player_serializer import Player_serializer_to_team
from ..query import Team_query


class Relation_serializer(serializers.ModelSerializer):

    player = Player_serializer_to_team()
    team_mate = Player_serializer_to_team()

    class Meta:
        model = Relation
        fields = ['id', 'player', 'team_mate',
                  'points', 'assists', 'rebounds']


class Relation_simple_serializer(serializers.ModelSerializer):

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
