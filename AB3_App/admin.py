from django.contrib import admin
from .models.Player import Player
from .models.Team import Team
from .models.Relation import Relation
# Register your models here.

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Relation)
