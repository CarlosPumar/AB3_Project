from rest_framework import serializers
from ..models.Relation import Relation
from ..serializers.Player_serializer import Player_serializer_to_team


class Relation_serializer(serializers.ModelSerializer):

    player = Player_serializer_to_team()
    team_mate = Player_serializer_to_team()

    class Meta:
        model = Relation
        fields = ['id', 'player', 'team_mate',
                  'points', 'assists', 'rebounds']


class Relation_simple_serializer(serializers.ModelSerializer):

    team_mate = Player_serializer_to_team(read_only=True)

    class Meta:
        model = Relation
        fields = ['id', 'team_mate', 'points', 'assists', 'rebounds']
