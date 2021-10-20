from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializer import Banker_serializer

from .models import Banker

# Create your views here.


class Banker_view(APIView):

    permission_classes = [IsAuthenticated]

    """ Obtener banker, si no devolver error"""

    def get_banker(self):

        try:
            return Banker.objects.get(pk=1)
        except Banker.DoesNotExist:
            raise Http404

    def get(self, request):

        banker = self.get_banker()
        serializer = Banker_serializer(banker)
        return Response(serializer.data)

    def post(self, request):

        serializer = Banker_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
