from ..models.Team import Team
from ..models.Player import Player
from django.forms.models import model_to_dict


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
