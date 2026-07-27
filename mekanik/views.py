from django.shortcuts import render, redirect, get_object_or_404
from .models import Mekanik, WorkOrder
from .forms import MekanikForm, WorkOrderForm, DetailServisForm


def dashboard_mekanik(request):
    return render(request, 'mekanik/dashboard.html')


def data_mekanik(request):
    mekanik = Mekanik.objects.all()

    context = {
        'mekanik': mekanik
    }

    return render(request, 'mekanik/data_mekanik.html', context)


def tambah_mekanik(request):
    if request.method == 'POST':
        form = MekanikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mekanik:data_mekanik')
    else:
        form = MekanikForm()

    return render(request, 'mekanik/tambah_mekanik.html', {
        'form': form
    })

def daftar_workorder(request):
    workorders = WorkOrder.objects.all()
    return render(request, 'mekanik/daftar_workorder.html', {
        'workorders': workorders
    })


def tambah_workorder(request):
    if request.method == 'POST':
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mekanik:daftar_workorder')
    else:
        form = WorkOrderForm()

    return render(request, 'mekanik/tambah_workorder.html', {
        'form': form
    })

def detail_servis(request, pk):
    workorder = get_object_or_404(WorkOrder, pk=pk)

    if request.method == 'POST':
        form = DetailServisForm(request.POST, instance=workorder)
        if form.is_valid():
            form.save()
            return redirect('mekanik:daftar_workorder')
    else:
        form = DetailServisForm(instance=workorder)

    return render(request, 'mekanik/detail_servis.html', {
        'workorder': workorder,
        'form': form,
    })