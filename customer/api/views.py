from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializer
from ..models import CustomUser
class AllUsers(APIView):
    def get(self, request):
        try:
            users = CustomUser.objects.all()
            serializer = UserSerializer(users, many=True)
            context={
                'success':True,
                "status" : status.HTTP_200_OK,
                "data":serializer.data
            }
            return Response(context)
        except Exception as error:
            context={
                'success':True,
                "status" : status.HTTP_200_OK,
                "data":str(error)
            }
            return Response(context)