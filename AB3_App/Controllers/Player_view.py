from rest_framework.response import Response
from ..serializers.Player_serializer import Player_serializer, Player_simple_serializer
from ..query import Player_query

from rest_framework import viewsets


class Player_view_set(viewsets.ModelViewSet):
    queryset = Player_query.get_list()
    serializer_class = Player_simple_serializer

    """ Redefinimos el metodo heredado retrieve """

    def retrieve(self, request, *args, **kwargs):
        player = self.get_object()
        serializer = Player_serializer(player)
        return Response(serializer.data)
