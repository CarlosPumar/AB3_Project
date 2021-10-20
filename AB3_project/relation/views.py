from rest_framework.response import Response
from .serializer import Relation_simple_serializer, Relation_serializer
from .models import Relation

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class Relation_view_set(viewsets.ModelViewSet):
    queryset = Relation.manager_extend.all()
    serializer_class = Relation_simple_serializer
    permission_classes = [IsAuthenticated]

    """ Redefinimos el metodo heredado retrieve """

    def retrieve(self, request, *args, **kwargs):
        player = self.get_object()
        serializer = Relation_serializer(player)
        return Response(serializer.data)
