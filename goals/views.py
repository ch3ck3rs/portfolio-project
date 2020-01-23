from django.shortcuts import render, get_object_or_404
from .models import Goal
from rest_framework import viewsets
from goals.serializers import GoalSeralizer


def allgoals(request):
    goals = Goal.objects
    return render(request, 'goals/allgoals.html', {'goals':goals})


def detail(request, goal_id):
    detail_goal = get_object_or_404(Goal, pk=goal_id)
    return render(request, 'goals/detail.html', {'goal':detail_goal})


class GoalViewSet(viewsets.ModelViewSet):
    """
    API endoint that allows goals to be viewed or edited
    """
    queryset = Goal.objects.all()  # .order_by('-date_joined')
    serializer_class = GoalSeralizer
