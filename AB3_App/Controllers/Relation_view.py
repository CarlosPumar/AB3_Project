from rest_framework.response import Response
from ..serializers.Relation_serializer import Relation_simple_serializer, Relation_serializer
from ..query import Relation_query

from rest_framework import viewsets


class Relation_view_set(viewsets.ModelViewSet):
    queryset = Relation_query.get_list()
    serializer_class = Relation_simple_serializer

    def retrieve(self, request, *args, **kwargs):
        player = self.get_object()
        serializer = Relation_serializer(player)
        return Response(serializer.data)
