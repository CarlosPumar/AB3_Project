
from django.http import response
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models.Team import Team
from ..serializers.Team_serializer import Team_simple_serializer, Team_serializer
from ..query import Team_query

from rest_framework import status


class Team_list_view(APIView):

    def get(self, request):
        team_list = Team_query.get_list()
        serializer = Team_simple_serializer(team_list, many=True)
        return Response(serializer.data)


class Team_detail_view(APIView):

    def get(self, request, id):
        """Obtencion objeto"""
        try:
            team = Team_query.get(id)
            serializer = Team_serializer(team)
            return Response(serializer.data)
        except:
            return Response("Error al acceder", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id=None):
        """Crear objeto"""

        serializer = Team_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'correct'})
        else:
            return Response("Error al crear equipo", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        """Actualizar objeto"""

        team = Team_query.get(id)
        serializer = Team_serializer(team, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'correct'})
        else:
            return Response("Error al crear equipo", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Eliminar objeto"""

        try:
            Team_query.delete(id)
            return Response({'status': 'correct'})
        except:
            return Response("Error al eliminar", status=status.HTTP_400_BAD_REQUEST)
