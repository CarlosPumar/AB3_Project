from ..models.Team import Team
from . import Player_query


def get_list():
    team_list = Team.objects.all()
    return team_list


def get(id):
    team = Team.objects.get(pk=id)
    return team


def delete(id):
    team = get(id)
    team.delete()


def create(name):
    team = Team(name)
    team.save()


def get_from_player(id):
    player = Player_query.get(id)
    return player.team
