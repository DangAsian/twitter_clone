from tweet.models import Tweet
from rest_framework import viewsets, permissions
from .serializers import TweetSerializer


#Cheat cheat cheat cheat
class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objets.all()
    permission_classes = [
        permissions:AllowAny
    ]
    serializer_class = TweetSerializer
