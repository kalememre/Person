from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, views , permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from PersonApp.permission import HasAccessToPersonCheckList
from .models import Person
from .serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class PersonCheckList(views.APIView):
    permission_classes = [HasAccessToPersonCheckList]
    def get(self, request):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
