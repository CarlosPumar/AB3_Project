from .models import Banker


""" Al ser un patron Singleton, solo habrá un único Banker con pk=1 """


def get():
    banker = Banker.objects.get(pk=1)
    return banker
