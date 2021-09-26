from ..models.Player import Player
from rest_framework import serializers


class Player_serializer_to_team(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ['id', 'name', 'state']
