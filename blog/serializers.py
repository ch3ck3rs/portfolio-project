from .models import Blog
from rest_framework import serializers


class BlogSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'pub_date', 'image', 'body']