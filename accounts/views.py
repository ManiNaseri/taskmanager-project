from rest_framework.views import APIView
from rest_framework.response import Response

class Rest(APIView):
    def get(self, request):
        name = request.query_params['name']
        return Response({"name": name})

    def post(self, request):
        name = request.data['name']
        return Response({"name": name})
    

