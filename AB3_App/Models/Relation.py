from django.db import models
from .Player import Player


class Relation(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='player')
    team_mate = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='team_mates')
    points = models.FloatField(default=0.0)
    assists = models.BooleanField(default=0.0)
    rebounds = models.BooleanField(default=0.0)

    def __str__(self):
        return self.player.name + ' - ' + self.team_mate.name
