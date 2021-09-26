from django.db import models
from .Team import Team

POSIBLE_STATES = {
    'AVAIABLE': 'AV',
    'DOUBTFUL': 'DB',
    'RULEDOUT': 'RO',
}

STATES_LIST = [
    (POSIBLE_STATES['AVAIABLE'], 'Avaiable'),
    (POSIBLE_STATES['DOUBTFUL'], 'Doubtful'),
    (POSIBLE_STATES['RULEDOUT'], 'Ruled Out'),
]


class Player(models.Model):
    name = models.CharField(max_length=300, unique=True)

    state = models.CharField(
        max_length=100, choices=STATES_LIST, default=POSIBLE_STATES['AVAIABLE'])
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name='players')

    def __str__(self):
        return self.name + ' - ' + self.state + ' - ' + self.team.name
