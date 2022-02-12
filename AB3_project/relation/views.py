from rest_framework.response import Response
from .serializer import Relation_simple_serializer, Relation_serializer
from .models import Relation

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class Relation_view_set(viewsets.ModelViewSet):
    queryset = Relation.manager_extend.all()
    serializer_class = Relation_simple_serializer
    permission_classes = [IsAuthenticated]

    """ Redefinimos el metodo heredado retrieve """

    def retrieve(self, request, *args, **kwargs):
        player = self.get_object()
        serializer = Relation_serializer(player)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        relations = Relation.manager_extend.filter(
            player=serializer.validated_data['player'], team_mate=serializer.validated_data['team_mate'])

        if relations:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
