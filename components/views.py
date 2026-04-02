from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ArrowShaftForm, VaneForm, NockForm, InsertForm, BroadheadForm


@login_required
def submit_shaft(request):
    if request.method == 'POST':
        form = ArrowShaftForm(request.POST)
        if form.is_valid():
            shaft = form.save(commit=False)
            shaft.submitted_by = request.user
            shaft.save()
            messages.success(request, 'Arrow shaft submitted for review. You can use it in your builds immediately.')
            return redirect('calculator:home')
    else:
        form = ArrowShaftForm()
    return render(request, 'components/submit.html', {'form': form, 'component_type': 'Arrow Shaft'})


@login_required
def submit_vane(request):
    if request.method == 'POST':
        form = VaneForm(request.POST)
        if form.is_valid():
            vane = form.save(commit=False)
            vane.submitted_by = request.user
            vane.save()
            messages.success(request, 'Vane submitted for review.')
            return redirect('calculator:home')
    else:
        form = VaneForm()
    return render(request, 'components/submit.html', {'form': form, 'component_type': 'Vane'})


@login_required
def submit_nock(request):
    if request.method == 'POST':
        form = NockForm(request.POST)
        if form.is_valid():
            nock = form.save(commit=False)
            nock.submitted_by = request.user
            nock.save()
            messages.success(request, 'Nock submitted for review.')
            return redirect('calculator:home')
    else:
        form = NockForm()
    return render(request, 'components/submit.html', {'form': form, 'component_type': 'Nock'})


@login_required
def submit_insert(request):
    if request.method == 'POST':
        form = InsertForm(request.POST)
        if form.is_valid():
            insert = form.save(commit=False)
            insert.submitted_by = request.user
            insert.save()
            messages.success(request, 'Insert submitted for review.')
            return redirect('calculator:home')
    else:
        form = InsertForm()
    return render(request, 'components/submit.html', {'form': form, 'component_type': 'Insert'})


@login_required
def submit_broadhead(request):
    if request.method == 'POST':
        form = BroadheadForm(request.POST)
        if form.is_valid():
            broadhead = form.save(commit=False)
            broadhead.submitted_by = request.user
            broadhead.save()
            messages.success(request, 'Broadhead submitted for review.')
            return redirect('calculator:home')
    else:
        form = BroadheadForm()
    return render(request, 'components/submit.html', {'form': form, 'component_type': 'Broadhead'})