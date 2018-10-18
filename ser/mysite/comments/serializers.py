from .models import Post #, Comment
from rest_framework import serializers


"""class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('created_on', 'author_name', 'author_email', 'text', 'objects')"""

class PostSerializer(serializers.HyperlinkedModelSerializer):
#    comments = CommentSerializer( many = True, read_only = True )
    class Meta:
        model = Post
        fields = ( 'id', 'created_on', 'text','author_name', 'author_email', 'restaurant_id', 'score', 'objects')