from ..utils.models import SingletonModel
from django.db import models

""" Banker implementa el patron Singleton """

class Banker(SingletonModel):
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

