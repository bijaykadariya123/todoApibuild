from .models import Todo
from rest_framework import serializers

## class TodoSerializer is a subclass of serializers.HyperLinkedModelSerializer.
## serializing and deserializing data into representation such as JSON. 
class TodoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Todo
        fields = ("id", "subject", "details")