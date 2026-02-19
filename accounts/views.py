from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
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


