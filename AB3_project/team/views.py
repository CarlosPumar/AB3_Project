from .serializer import Team_simple_serializer
from . import query as Team_query

from rest_framework import viewsets


class Team_view_set(viewsets.ModelViewSet):

    queryset = Team_query.get_list()
    serializer_class = Team_simple_serializer