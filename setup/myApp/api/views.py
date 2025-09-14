from rest_framework.viewsets import ModelViewSet
from ..models import myApp
from .serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = myApp.objects.all()
    serializer_class = PostSerializer
