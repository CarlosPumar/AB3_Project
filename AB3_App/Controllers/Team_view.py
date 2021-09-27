from ..serializers.Team_serializer import Team_simple_serializer, Team_serializer
from ..query import Team_query

from rest_framework import viewsets


class Team_view_set(viewsets.ModelViewSet):

    queryset = Team_query.get_list()
    serializer_class = Team_simple_serializer


class Team_view_set_for_detail(Team_view_set):

    serializer_class = Team_serializer
