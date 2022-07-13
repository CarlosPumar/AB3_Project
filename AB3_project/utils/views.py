from rest_framework.views import APIView
from rest_framework.response import Response

from ab3_project.twitter.stream import Stream_Twitter
from ab3_project.utils.data import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, ID_ACCOUNT

from .data import POSIBLE_STATES

from rest_framework.permissions import IsAuthenticated


class States_view(APIView):

    def get(self, request):
        return Response(POSIBLE_STATES)
