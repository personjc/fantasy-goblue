from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Manager, Season
from .serializers import ManagerSerializer, SeasonSerializer

class ManagerApiListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        managers = Manager.objects.all()
        serializer = ManagerSerializer(managers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'id': request.data.get('id'),
            'name': request.data.get('name')
        }

        serializer = ManagerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SeasonApiListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        seasons = Season.objects.all()
        serializer = SeasonSerializer(seasons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'season': request.data.get('season'),
            'league_id': request.data.get('league_id'),
            'game_id': request.data.get('game_id')
        }

        serializer = SeasonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    