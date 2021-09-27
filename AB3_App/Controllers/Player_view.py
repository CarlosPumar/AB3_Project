from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.Player import Player
from ..serializers.Player_serializer import Player_serializer, Player_simple_serializer, Player_no_relation_serializer
from ..query import Player_query


class Player_list_view(APIView):

    def get(self, request):
        """Obtecion lista jugadores"""

        player_list = Player_query.get_list()
        serializer = Player_no_relation_serializer(player_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Player_simple_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "correct"})
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class Player_detail_simple_view(APIView):

    def get(self, request, id):
        player = Player_query.get(id)
        serialzer = Player_simple_serializer(player, many=False)
        return Response(serialzer.data)

    def put(self, request, id):

        try:
            player = Player_query.get(id)
        except:
            return Response("Error al modificar jugador", status=status.HTTP_204_NO_CONTENT)

        serializer = Player_simple_serializer(
            instance=player, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "correct"})
        else:
            return Response("Error al modificar jugador", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):

        try:
            Player_query.delete(id)
            return Response({'status': 'correct'})
        except:
            return Response("Error al eliminar jugador", status=status.HTTP_400_BAD_REQUEST)


class Player_detail_relation_view(APIView):

    def get(self, request, id):
        player = Player_query.get(id)
        serialzer = Player_serializer(player, many=False)
        return Response(serialzer.data)
