from rest_framework.serializers import ModelSerializer
from ..models import myApp

class PostSerializer(ModelSerializer):
    class Meta:
        model = myApp
        fields = ('id', 'title', 'body')