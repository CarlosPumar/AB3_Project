from django.db import models
from ..player.models import Player


class Relation_Manager(models.Manager):

    def get_relation_from_player(self, name):
        player = Player.manager_extend.get(name=name)

        relations = super().filter(
            player=player, team_mate__state="AV")
        return relations
