from rest_framework import serializers
from .models import Job


class JobSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['image', 'summary']