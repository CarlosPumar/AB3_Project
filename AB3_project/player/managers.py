from django.db import models


class Player_Manager(models.Manager):

    def player_exists(self, player_name):
        try:
            player = super().get(name=player_name)
        except:
            player = None

        if player == None:
            return False
        else:
            return True

    def modify_state(self, player_name, state):
        player = super().get(name=player_name)
        player.state = state
        player.save()

    def get_state_from_player(self, player_name):
        player = super().get(name=player_name)
        return player.state
