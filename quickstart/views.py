from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSeralizer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSeralizer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endoint that allows users to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
