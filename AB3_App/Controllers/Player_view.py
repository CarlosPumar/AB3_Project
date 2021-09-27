from rest_framework.decorators import action
from rest_framework.response import Response
from ..serializers.Player_serializer import Player_serializer, Player_simple_serializer, Player_no_relation_serializer
from ..query import Player_query

from rest_framework import viewsets


class Player_view_set(viewsets.ModelViewSet):
    queryset = Player_query.get_list()
    serializer_class = Player_simple_serializer


class Player_view_set_for_detail(Player_view_set):

    @action(detail=False)
    def get_all(self, request, pk):

        player = Player_query.get(pk)
        serializer = Player_serializer(player)
        return Response(serializer.data)
