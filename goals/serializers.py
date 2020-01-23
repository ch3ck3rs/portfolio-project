from .models import Goal
from rest_framework import serializers


class GoalSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goal
        fields = ['title', 'set_date', 'target_date', 'image', 'body', 'set_back']