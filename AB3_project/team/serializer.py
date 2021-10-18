from rest_framework import serializers
from .models import Team


class Team_simple_serializer(serializers.ModelSerializer):

    """
    {
        "id": x,
        "name": "x"
    }
    """

    class Meta:

        model = Team
        fields = ['id', 'name']
