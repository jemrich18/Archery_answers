from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BowSetup, ArrowBuild
from .forms import BowSetupForm, ArrowBuildForm
from calculator.models import AnimalThreshold


@login_required
def builder_home(request):
    bows = BowSetup.objects.filter(user=request.user)
    builds = ArrowBuild.objects.filter(user=request.user).select_related('bow', 'shaft', 'vane', 'nock', 'insert', 'broadhead')
    thresholds = AnimalThreshold.objects.all()
    return render(request, 'builder/home.html', {
        'bows': bows,
        'builds': builds,
        'thresholds': thresholds,
    })


@login_required
def create_bow(request):
    if request.method == 'POST':
        form = BowSetupForm(request.POST)
        if form.is_valid():
            bow = form.save(commit=False)
            bow.user = request.user
            bow.save()
            messages.success(request, f'Bow "{bow.name}" saved!')
            return redirect('builder:home')
    else:
        form = BowSetupForm()
    return render(request, 'builder/create_bow.html', {'form': form})


@login_required
def create_build(request, bow_id):
    bow = get_object_or_404(BowSetup, id=bow_id, user=request.user)
    if request.method == 'POST':
        form = ArrowBuildForm(request.POST, user=request.user)
        if form.is_valid():
            build = form.save(commit=False)
            build.user = request.user
            build.bow = bow
            build.save()  # This triggers calculate() in the model
            messages.success(request, f'Build "{build.name}" created! Speed: {build.arrow_speed:.1f} FPS | KE: {build.kinetic_energy:.1f} ft-lbs')
            return redirect('builder:home')
    else:
        form = ArrowBuildForm(user=request.user)
    return render(request, 'builder/create_build.html', {'form': form, 'bow': bow})


@login_required
def my_builds(request):
    builds = ArrowBuild.objects.filter(user=request.user).select_related('bow', 'shaft', 'vane', 'nock', 'insert', 'broadhead')
    thresholds = AnimalThreshold.objects.all()
    return render(request, 'builder/my_builds.html', {'builds': builds, 'thresholds': thresholds})