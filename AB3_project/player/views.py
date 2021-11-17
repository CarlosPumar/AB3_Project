from rest_framework.response import Response
from .serializer import Player_simple_serializer
from .serializer_standar import Player_serializer
from .models import Player
from rest_framework import status
import json

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class Player_view_set(viewsets.ModelViewSet):
    queryset = Player.manager_extend.all()
    serializer_class = Player_simple_serializer
    #permission_classes = [IsAuthenticated]

    """ Redefinimos el metodo heredado retrieve """

    def retrieve(self, request, *args, **kwargs):

        player = self.get_object()
        serializer = Player_serializer(player)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):

        new_player = Player.manager_extend.update(request.data)
        new_serializer = self.get_serializer(new_player)

        return Response(new_serializer.data)
