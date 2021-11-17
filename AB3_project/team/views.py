from django.db.models import query
from rest_framework.decorators import permission_classes
from .serializer import Team_serializer
from .models import Team
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class Team_view_set(viewsets.ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = Team_serializer
    #permission_classes = [IsAuthenticated]
