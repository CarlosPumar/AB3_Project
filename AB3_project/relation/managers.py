from django.db import models

from ..player.models import Player


class Relation_Manager(models.Manager):

    def get_relation_from_player(self, name):
        player = Player.manager_extend.get(name=name)

        relations = super().filter(
            player=player, team_mate__state="AV")
        return relations

    def is_relation_duplicate(self, player_id, team_mate_id):
        relations = super().filter(player=player_id)

        for relation in relations:
            if relation.team_mate.id == team_mate_id:
                return True

        return False
