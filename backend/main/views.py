from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Developer
from .serializers import DeveloperSerializer

class DeveloperView(APIView):

    def get_object(self):
        return Developer.objects.all()

    def get(self, request):
        user = self.get_object()
        serializer = DeveloperSerializer(user, many=True)
        return Response({'get' : serializer.data})