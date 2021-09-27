from django.urls import path
from .Team_view import Team_list_view, Team_detail_view

urlpatterns = [
    # Team
    path('team/list', Team_list_view.as_view(), name='team_list_view '),
    path('team/<int:id>', Team_detail_view.as_view(), name='team_detail_view '),
]
