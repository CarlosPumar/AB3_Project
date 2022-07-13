from django.contrib.auth.models import User
from .serializer import User_serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import jwt
from ..settings import SECRET_KEY


from .serializer import User_serializer


class User_view(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        encoded_jwt = request.headers['Authorization']
        encoded_jwt = encoded_jwt.split(" ")
        encoded_jwt = encoded_jwt[1]

        data = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])
        user = User.objects.get(pk=data['user_id'])
        user_serializer = User_serializer(user)

        return Response(user_serializer.data)
