from django.shortcuts import render
from .models import Job


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})


def sup_home(request):
    jobs = Job.objects
    return render(request, 'jobs/sup_home.html', {'jobs':jobs})
