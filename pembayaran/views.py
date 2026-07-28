from django.shortcuts import render, redirect, get_object_or_404
from .models import Sparepart
from .forms import SparepartForm
from .models import Sparepart, JasaServis
from .forms import SparepartForm, JasaServisForm
from .models import Pembayaran
from .forms import PembayaranForm
from .models import Pembayaran
from .forms import PembayaranForm
from mekanik.models import WorkOrder
from django.http import HttpResponse
from reportlab.pdfgen import canvas

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
    
from mekanik.models import WorkOrder



def daftar_pembayaran(request):

    pembayaran = Pembayaran.objects.all()


    return render(
        request,
        'pembayaran/daftar_pembayaran.html',
        {
            'pembayaran': pembayaran
        }
    )




def tambah_pembayaran(request):


    if request.method == "POST":


        form = PembayaranForm(request.POST)


        if form.is_valid():


            pembayaran = form.save(commit=False)


            pembayaran.total_bayar = (
                pembayaran.total_sparepart +
                pembayaran.total_jasa
            )


            pembayaran.status = "Lunas"


            pembayaran.save()


            return redirect(
                'daftar_pembayaran'
            )


    else:


        form = PembayaranForm()



    return render(
        request,
        'pembayaran/form_pembayaran.html',
        {
            'form':form
        }
    )





def detail_pembayaran(request, pk):


    pembayaran = get_object_or_404(
        Pembayaran,
        pk=pk
    )


    return render(
        request,
        'pembayaran/detail_pembayaran.html',
        {
            'pembayaran':pembayaran
        }
    )

def daftar_pembayaran(request):

    pembayaran = Pembayaran.objects.all().order_by("-id")


    return render(
        request,
        'pembayaran/daftar_pembayaran.html',
        {
            'pembayaran': pembayaran
        }
    )



def tambah_pembayaran(request):

    if request.method == "POST":

        form = PembayaranForm(request.POST)


        if form.is_valid():

            pembayaran = form.save(commit=False)


            pembayaran.total_bayar = (
                pembayaran.total_sparepart +
                pembayaran.total_jasa
            )


            pembayaran.status = "Lunas"


            pembayaran.save()


            return redirect(
                'daftar_pembayaran'
            )


    else:

        form = PembayaranForm()



    return render(
        request,
        'pembayaran/form_pembayaran.html',
        {
            'form': form
        }
    )



def detail_pembayaran(request, pk):

    pembayaran = get_object_or_404(
        Pembayaran,
        pk=pk
    )


    return render(
        request,
        'pembayaran/detail_pembayaran.html',
        {
            'pembayaran': pembayaran
        }
    )
    
def cetak_invoice(request, pk):

    pembayaran = get_object_or_404(
        Pembayaran,
        pk=pk
    )


    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        f'attachment; filename="invoice_{pembayaran.id}.pdf"'
    )


    pdf = canvas.Canvas(response)


    pdf.drawString(
        100,
        800,
        "BENGKELKU - INVOICE PEMBAYARAN"
    )


    pdf.drawString(
        100,
        760,
        f"ID Pembayaran : {pembayaran.id}"
    )


    pdf.drawString(
        100,
        730,
        f"Work Order : {pembayaran.workorder}"
    )


    pdf.drawString(
        100,
        700,
        f"Total Sparepart : Rp {pembayaran.total_sparepart}"
    )


    pdf.drawString(
        100,
        670,
        f"Total Jasa : Rp {pembayaran.total_jasa}"
    )


    pdf.drawString(
        100,
        640,
        f"Total Bayar : Rp {pembayaran.total_bayar}"
    )


    pdf.drawString(
        100,
        610,
        f"Metode : {pembayaran.metode}"
    )


    pdf.drawString(
        100,
        580,
        f"Status : {pembayaran.status}"
    )


    pdf.save()


    return response