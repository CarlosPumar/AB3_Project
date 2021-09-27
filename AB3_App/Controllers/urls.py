from django.urls import path
from .Team_view import Team_list_view, Team_detail_view
from .Player_view import Player_list_view, Player_detail_view, Player_detail_simple_view

urlpatterns = [
    # Team
    path('team/list', Team_list_view.as_view(), name='team_list_view '),
    path('team/<int:id>', Team_detail_view.as_view(), name='team_detail_view '),

    # Player
    path('player/list', Player_list_view.as_view(), name="player_list_view"),
    path('player/<int:id>', Player_detail_view.as_view(),
         name="player_detail_view"),
    path('player/simple/<int:id>', Player_detail_simple_view.as_view(),
         name="player_detail_simple_view"),
]
