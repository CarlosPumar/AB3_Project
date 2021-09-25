from ..models.Team import Team
from ..models.Player import Player
from django.forms.models import model_to_dict


def get_team_list():
    team_list = list(Team.objects.all().values())
    return team_list


def get_team_by_id(id):
    team = Team.objects.get(pk=id)
    player_list = list(Player.objects.filter(team=team).values())

    team_dict = model_to_dict(team)
    team_dict['player_list'] = player_list

    return team_dict
