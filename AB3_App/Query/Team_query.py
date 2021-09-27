from ..models.Team import Team


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
