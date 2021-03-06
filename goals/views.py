from django.shortcuts import render, get_object_or_404
from .models import Goal

# Create your views here.


def allgoals(request):
    goals = Goal.objects
    return render(request, 'goals/allgoals.html', {'goals':goals})


def detail(request, goal_id):
    detail_goal = get_object_or_404(Goal, pk=goal_id)
    return render(request, 'goals/detail.html', {'goal':detail_goal})

