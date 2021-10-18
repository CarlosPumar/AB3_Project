from django.db import models
from ..team.models import Team
from .managers import Player_Manager
from ..utils.data import POSIBLE_STATES

STATES_LIST = [
    (POSIBLE_STATES['AVAIABLE']['code'], 'Avaiable'),
    (POSIBLE_STATES['PROBABLE']['code'], 'Probable'),
    (POSIBLE_STATES['QUESTIONABLE']['code'], 'Questionable'),
    (POSIBLE_STATES['DOUBTFUL']['code'], 'Doubtful'),
    (POSIBLE_STATES['RULEDOUT']['code'], 'Ruled Out'),
]


class Player(models.Model):
    name = models.CharField(max_length=300, unique=True)

    state = models.CharField(
        max_length=100, choices=STATES_LIST, default=POSIBLE_STATES['AVAIABLE']['code'])
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name='players')

    manager_extend = Player_Manager()

    def __str__(self):
        return self.name + ' - ' + self.state + ' - ' + self.team.name
