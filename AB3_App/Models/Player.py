from django.db import models
from .Team import Team


class Player(models.Model):
    name = models.CharField(max_length=300, unique=True)

    AVAIABLE = 'AV'
    DOUBTFUL = 'DB'
    RULEDOUT = 'RO'

    STATES_LIST = [
        (AVAIABLE, 'Avaiable'),
        (DOUBTFUL, 'Doubtful'),
        (RULEDOUT, 'Ruled Out'),
    ]

    state = models.CharField(
        max_length=2, choices=STATES_LIST, default=AVAIABLE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name + ' - ' + self.state + ' - ' + self.team.name
