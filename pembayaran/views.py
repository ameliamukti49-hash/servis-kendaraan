from django.shortcuts import render, redirect, get_object_or_404
from .models import Sparepart
from .forms import SparepartForm
from .models import Sparepart, JasaServis
from .forms import SparepartForm, JasaServisForm


def daftar_sparepart(request):
    spareparts = Sparepart.objects.all()
    return render(request, 'pembayaran/daftar_sparepart.html', {
        'spareparts': spareparts
    })


def tambah_sparepart(request):
    if request.method == 'POST':
        form = SparepartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_sparepart')
    else:
        form = SparepartForm()

    return render(request, 'pembayaran/form_sparepart.html', {
        'form': form
    })


def edit_sparepart(request, pk):
    sparepart = get_object_or_404(Sparepart, pk=pk)

    if request.method == 'POST':
        form = SparepartForm(request.POST, instance=sparepart)
        if form.is_valid():
            form.save()
            return redirect('daftar_sparepart')
    else:
        form = SparepartForm(instance=sparepart)

    return render(request, 'pembayaran/form_sparepart.html', {
        'form': form
    })


def hapus_sparepart(request, pk):
    sparepart = get_object_or_404(Sparepart, pk=pk)

    if request.method == 'POST':
        sparepart.delete()
        return redirect('daftar_sparepart')

    return render(request, 'pembayaran/hapus_sparepart.html', {
        'sparepart': sparepart
    })

def daftar_jasa(request):
    jasa = JasaServis.objects.all()
    return render(request, 'pembayaran/daftar_jasa.html', {
        'jasa': jasa
    })


def tambah_jasa(request):
    if request.method == 'POST':
        form = JasaServisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_jasa')
    else:
        form = JasaServisForm()

    return render(request, 'pembayaran/form_jasa.html', {
        'form': form
    })


def edit_jasa(request, pk):
    jasa = get_object_or_404(JasaServis, pk=pk)

    if request.method == 'POST':
        form = JasaServisForm(request.POST, instance=jasa)
        if form.is_valid():
            form.save()
            return redirect('daftar_jasa')
    else:
        form = JasaServisForm(instance=jasa)

    return render(request, 'pembayaran/form_jasa.html', {
        'form': form
    })


def hapus_jasa(request, pk):
    jasa = get_object_or_404(JasaServis, pk=pk)

    if request.method == 'POST':
        jasa.delete()
        return redirect('daftar_jasa')

    return render(request, 'pembayaran/hapus_jasa.html', {
        'jasa': jasa
    })