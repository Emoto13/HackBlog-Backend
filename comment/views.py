from rest_framework import viewsets
from comment.serializers import CommentSerializer
from comment.models import Comment

# Create your views here.


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
