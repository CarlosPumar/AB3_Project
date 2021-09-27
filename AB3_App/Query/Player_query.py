from ..models.Player import Player


def get_list():
    players = Player.objects.all()
    return players


def get(id):
    player = Player.objects.get(pk=id)
    return player


def delete(id):
    player = get(id)
    player.delete()
