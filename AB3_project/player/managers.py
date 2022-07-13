from django.db import models
import json
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


class Player_Manager(models.Manager):

    def player_exists(self, player_name):
        try:
            player = super().get(name=player_name)
        except:
            player = None

        if player == None:
            return False
        else:
            return True

    def modify_state(self, player_name, state):
        player = super().get(name=player_name)
        player.state = state
        player.save()

    def get_state_from_player(self, player_name):
        player = super().get(name=player_name)
        return player.state

    def update(self, new_player):

        from .serializer_standar import Player_serializer
        from ..team.models import Team

        player = super().get(pk=new_player['id'])
        super().get(pk=new_player['id'])
        player_serializer = Player_serializer(player)
        player_dict = self.__serializer_to_dict(player_serializer)

        if player_dict['team']['id'] != new_player['team']:
            self.__clear_relation(player)

        player.id = new_player['id']
        player.name = new_player['name']
        player.state = new_player['state']

        team = Team.objects.get(pk=new_player['team'])
        player.team = team

        player.save()

        return player

    def __clear_relation(self, player):

        from ..relation.models import Relation
        relations = Relation.manager_extend.filter(player=player).delete()

    def __serializer_to_dict(self, serializer):
        json = JSONRenderer().render(serializer.data)
        stream = io.BytesIO(json)
        data = JSONParser().parse(stream)

        return data
