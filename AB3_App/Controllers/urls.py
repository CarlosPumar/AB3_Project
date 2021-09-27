from django.urls import path, include
from .Team_view import Team_view_set, Team_view_set_for_detail
from .Player_view import Player_view_set, Player_view_set_for_detail

from rest_framework.routers import DefaultRouter

""" Team views """
team_list = Team_view_set.as_view({
    'get': 'list',
    'post': 'create',
})

team_detail = Team_view_set_for_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

""" Plater views """
player_list = Player_view_set.as_view({
    'get': 'list',
    'post': 'create',
})

player_detail = Player_view_set.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

player_get_all = Player_view_set_for_detail.as_view({
    'get': 'get_all',
})


urlpatterns = [
    # Team
    path('team/', team_list, name='team-list'),
    path('team/<int:pk>', team_detail, name='team-detail'),

    # Player
    path('player/', player_list, name='player-list'),
    path('player/<int:pk>', player_detail, name='player-detail'),
    path('player/<int:pk>/get_all', player_get_all, name='player-get-all'),
]
