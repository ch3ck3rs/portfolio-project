from django.shortcuts import render
from .models import Sup

# Create your views here.

def sup_home(request):
    jobs = Job.objects
    return render(request, 'jobs/sup_home.html', {'jobs':jobs})