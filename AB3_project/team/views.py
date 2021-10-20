from .serializer import Team_simple_serializer
from .models import Team
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class Team_view_set(viewsets.ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = Team_simple_serializer
    permission_classes = [IsAuthenticated]
