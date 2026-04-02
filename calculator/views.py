from django.shortcuts import render
from .models import AnimalThreshold

# Create your views here.

def home(request):
    thresholds = AnimalThreshold.objects.all()
    return render(request, 'home.html', {'thresholds': thresholds})
