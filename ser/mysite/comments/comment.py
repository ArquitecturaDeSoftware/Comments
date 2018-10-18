from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post #, Comment 
from .serializers import PostSerializer #, CommentSerializer 
from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET', 'POST'])
def post_list(request, format = None):
    
    if request.method == 'GET':
        posts = Post.objects.all() 
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        return Post.objects.filter(restaurant_id=restaurant_id)

