from django.shortcuts import render
from .models import Job
from rest_framework import viewsets
from jobs.serializers import JobSeralizer


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})


class JobViewSet(viewsets.ModelViewSet):
    """
    API endoint that allows jobs to be viewed or edited
    """
    queryset = Job.objects.all()  # .order_by('-date_joined')
    serializer_class = JobSeralizer

