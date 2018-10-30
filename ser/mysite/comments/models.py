from djongo import models
from mongoengine import Document, EmbeddedDocument, fields, ListField

#comments = ListField(EmbeddedModelField('Comment')) # <---
from django.core.validators import MinValueValidator, MaxValueValidator

"""class Comment(EmbeddedDocument):
    created_on = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length = 200)
    author_email = models.CharField(max_length = 200)
    text = models.TextField()
    objects = models.Manager()
    objects.model = models
    def __str__(self):
        return self.text"""

count = 0

class Post(models.Model):
    id = models.AutoField( primary_key=True )
    restaurant_id = models.TextField( )
    score = models.IntegerField( validators = [ MinValueValidator( 0 ), MaxValueValidator( 5 ) ] )
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField()
    author_name = models.CharField(max_length = 200)
    author_email = models.CharField(max_length = 200)
 #   comments = fields.ListField(fields.EmbeddedDocumentField('Comment'))
    objects = models.Manager()
    objects.model = models
    def __str__(self):
        return self.text
