from rest_framework.views import APIView
from rest_framework.response import Response

from .data import POSIBLE_STATES


class States_view(APIView):

    def get(self, request):
        return Response(POSIBLE_STATES)
