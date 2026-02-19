from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from .models import User

class UserRegisterApiView(APIView):
    def post(self, request):
        serializeData = UserSerializer(data=request.POST)
        if serializeData.is_valid():
            User.objects.create_user(
                username= serializeData.validated_data["username"],
                email= serializeData.validated_data["email"],
                password= serializeData.validated_data["password"]
            )
            return Response(serializeData.data)
        return Response(serializeData.errors)


class UserLoginApiView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            return Response({"message": "user logged in successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "user does not exist"}, status=status.HTTP_401_UNAUTHORIZED)

