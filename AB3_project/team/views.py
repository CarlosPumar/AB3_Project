from .serializer import Team_simple_serializer
from .models import Team
from rest_framework import viewsets


class Team_view_set(viewsets.ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = Team_simple_serializer
