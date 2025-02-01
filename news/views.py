from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .api.pagination import NewsPagination
from .models import ModelNews
from news.api.serializers import ModelNewsSerializer

class NewsListCreateView(APIView, NewsPagination):
    permission_classes = [IsAuthenticated]  # Require authentication

    def get(self, request):
        news = ModelNews.objects.all()
        results = self.paginate_queryset(news, request)
        serializer = ModelNewsSerializer(news, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ModelNewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewsDetailView(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication

    def get_object(self, pk):
        try:
            return ModelNews.objects.get(pk=pk)
        except ModelNews.DoesNotExist:
            return None

    def get(self, request, pk):
        news = self.get_object(pk)
        if not news:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ModelNewsSerializer(news)
        return Response(serializer.data)

    def put(self, request, pk):
        news = self.get_object(pk)
        if not news:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ModelNewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        news = self.get_object(pk)
        if not news:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
