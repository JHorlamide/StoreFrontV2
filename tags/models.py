from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
  label = models.CharField(max_length=255)
  
class TaggedItem(models.Model):
  # What tag is applied to what object?
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
  
  # How can we tag an object?
  # Type of object (Product, Video, Article, etc...)
  # ID of the object
  
  # Note: 1: The ContentType comes with Django for representing as abstract class.
  # 2: Using ContentTypes we can create generic relationships between our models.
  # 3: ContentType is a model that represent the type of an object in our application.
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  
  # This enables us to get the actual object this tag is applied to.
  # Using this field, we can read the actual object that a particular tag is applied to.
  content_object = GenericForeignKey()
  
   
