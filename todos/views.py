# from django.shortcuts import render
from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer

# viewsets has already built in crud routes in django frame_work we are just inherting them from the parent class(viewset class)
# permission class will determines if the person can access the data.

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    # this will get all the list to Todo objects
    queryset = Todo.objects.all()
    # this will serialize and deserialize queryset and model instances
    # any time it pulls a data from our query set to update, delete or crud functionality and when it send backs it will serializes the date
    serializer_class= TodoSerializer
    
    # permission class will determines if the person can access the data.
    permission_classes = [permissions.AllowAny]