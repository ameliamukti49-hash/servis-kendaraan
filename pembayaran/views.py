from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Sparepart,
    JasaServis,
    Pembayaran,
    DetailSparepart,
    DetailJasa,
)

from .forms import (
    SparepartForm,
    JasaServisForm,
    PembayaranForm,
    DetailSparepartForm,
    DetailJasaForm,
)

from mekanik.models import WorkOrder
from django.db.models import Sum
from decimal import Decimal


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

def daftar_pembayaran(request):
    pembayaran = Pembayaran.objects.all().order_by('-tanggal_bayar')

    return render(
        request,
        'pembayaran/daftar_pembayaran.html',
        {
            'pembayaran': pembayaran
        }
    )

def tambah_pembayaran(request, workorder_id):

    workorder = get_object_or_404(
        WorkOrder,
        pk=workorder_id
    )

    total_sparepart = DetailSparepart.objects.filter(
        workorder=workorder
    ).aggregate(
        total=Sum('subtotal')
    )['total'] or Decimal('0')

    total_jasa = DetailJasa.objects.filter(
        workorder=workorder
    ).aggregate(
        total=Sum('subtotal')
    )['total'] or Decimal('0')

    total_bayar = total_sparepart + total_jasa

    if request.method == 'POST':

        form = PembayaranForm(request.POST)

        if form.is_valid():

            pembayaran = form.save(commit=False)

            pembayaran.workorder = workorder
            pembayaran.total_sparepart = total_sparepart
            pembayaran.total_jasa = total_jasa
            pembayaran.total_bayar = total_bayar

            pembayaran.save()

            return redirect('daftar_pembayaran')

    else:
        form = PembayaranForm()

    return render(
        request,
        'pembayaran/form_pembayaran.html',
        {
            'form': form,
            'workorder': workorder,
            'total_sparepart': total_sparepart,
            'total_jasa': total_jasa,
            'total_bayar': total_bayar,
        }
    )

def edit_pembayaran(request, pk):

    pembayaran = get_object_or_404(
        Pembayaran,
        pk=pk
    )

    total_sparepart = DetailSparepart.objects.filter(
        workorder=pembayaran.workorder
    ).aggregate(
        total=Sum('subtotal')
    )['total'] or Decimal('0')

    total_jasa = DetailJasa.objects.filter(
        workorder=pembayaran.workorder
    ).aggregate(
        total=Sum('subtotal')
    )['total'] or Decimal('0')

    total_bayar = total_sparepart + total_jasa

    if request.method == 'POST':

        form = PembayaranForm(
            request.POST,
            instance=pembayaran
        )

        if form.is_valid():

            pembayaran = form.save(commit=False)

            pembayaran.total_sparepart = total_sparepart
            pembayaran.total_jasa = total_jasa
            pembayaran.total_bayar = total_bayar

            pembayaran.save()

            return redirect('daftar_pembayaran')

    else:

        form = PembayaranForm(instance=pembayaran)

    return render(
        request,
        'pembayaran/form_pembayaran.html',
        {
            'form': form,
            'workorder': pembayaran.workorder,
            'total_sparepart': total_sparepart,
            'total_jasa': total_jasa,
            'total_bayar': total_bayar,
            'edit': True,
        }
    )

def invoice(request, pk):

    pembayaran = get_object_or_404(
        Pembayaran,
        pk=pk
    )

    detail_sparepart = DetailSparepart.objects.filter(
        workorder=pembayaran.workorder
    )

    detail_jasa = DetailJasa.objects.filter(
        workorder=pembayaran.workorder
    )

    return render(
        request,
        'pembayaran/invoice.html',
        {
            'pembayaran': pembayaran,
            'detail_sparepart': detail_sparepart,
            'detail_jasa': detail_jasa,
        }
    )

def hapus_pembayaran(request, pk):

    pembayaran = get_object_or_404(
        Pembayaran,
        pk=pk
    )

    if request.method == "POST":
        pembayaran.delete()
        return redirect('daftar_pembayaran')

    return render(
        request,
        'pembayaran/hapus_pembayaran.html',
        {
            'pembayaran': pembayaran
        }
    )

def daftar_detail_sparepart(request, workorder_id):

    workorder = get_object_or_404(
        WorkOrder,
        pk=workorder_id
    )

    detail_sparepart = DetailSparepart.objects.filter(
        workorder=workorder
    )

    return render(
        request,
        'pembayaran/daftar_detail_sparepart.html',
        {
            'workorder': workorder,
            'detail_sparepart': detail_sparepart,
        }
    )


def tambah_detail_sparepart(request, workorder_id):

    workorder = get_object_or_404(
        WorkOrder,
        pk=workorder_id
    )

    if request.method == 'POST':

        form = DetailSparepartForm(request.POST)

        if form.is_valid():

            detail = form.save(commit=False)

            detail.workorder = workorder

            detail.save()

            return redirect(
                'daftar_detail_sparepart',
                workorder_id=workorder.id
            )

    else:

        form = DetailSparepartForm()

    return render(
        request,
        'pembayaran/form_detail_sparepart.html',
        {
            'form': form,
            'workorder': workorder,
        }
    )