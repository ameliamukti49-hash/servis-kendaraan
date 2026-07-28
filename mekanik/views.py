from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Mekanik, WorkOrder
from .forms import MekanikForm, WorkOrderForm, DetailServisForm



@login_required
def dashboard_mekanik(request):

    total_workorder = WorkOrder.objects.count()

    diproses = WorkOrder.objects.filter(
        status='diproses'
    ).count()


    dikerjakan = WorkOrder.objects.filter(
        status='dikerjakan'
    ).count()


    selesai = WorkOrder.objects.filter(
        status='selesai'
    ).count()



    workorders = WorkOrder.objects.all().order_by('-id')[:5]


    context = {

        'total_workorder': total_workorder,

        'diproses': diproses,

        'dikerjakan': dikerjakan,

        'selesai': selesai,

        'workorders': workorders,

    }


    return render(
        request,
        'mekanik/dashboard.html',
        context
    )




# ==========================
# DATA MEKANIK
# ==========================


def data_mekanik(request):

    mekanik = Mekanik.objects.all()


    return render(
        request,
        'mekanik/data_mekanik.html',
        {
            'mekanik': mekanik
        }
    )





def tambah_mekanik(request):

    if request.method == 'POST':

        form = MekanikForm(request.POST)


        if form.is_valid():

            form.save()

            return redirect(
                'mekanik:data_mekanik'
            )


    else:

        form = MekanikForm()



    return render(
        request,
        'mekanik/tambah_mekanik.html',
        {
            'form': form
        }
    )





def edit_mekanik(request, pk):

    mekanik = get_object_or_404(
        Mekanik,
        pk=pk
    )


    if request.method == 'POST':

        form = MekanikForm(
            request.POST,
            instance=mekanik
        )


        if form.is_valid():

            form.save()

            return redirect(
                'mekanik:data_mekanik'
            )


    else:

        form = MekanikForm(
            instance=mekanik
        )


    return render(
        request,
        'mekanik/edit_mekanik.html',
        {
            'form': form
        }
    )





def hapus_mekanik(request, pk):

    mekanik = get_object_or_404(
        Mekanik,
        pk=pk
    )


    mekanik.delete()


    return redirect(
        'mekanik:data_mekanik'
    )





# ==========================
# WORK ORDER
# ==========================


def daftar_workorder(request):

    workorders = WorkOrder.objects.all()


    return render(
        request,
        'mekanik/daftar_workorder.html',
        {
            'workorders': workorders
        }
    )





def tambah_workorder(request):

    if request.method == 'POST':

        form = WorkOrderForm(
            request.POST
        )


        if form.is_valid():

            form.save()

            return redirect(
                'mekanik:daftar_workorder'
            )


    else:

        form = WorkOrderForm()



    return render(
        request,
        'mekanik/tambah_workorder.html',
        {
            'form': form
        }
    )





def detail_servis(request, pk):

    workorder = get_object_or_404(
        WorkOrder,
        pk=pk
    )


    if request.method == 'POST':

        form = DetailServisForm(
            request.POST,
            instance=workorder
        )


        if form.is_valid():

            form.save()

            return redirect(
                'mekanik:daftar_workorder'
            )


    else:

        form = DetailServisForm(
            instance=workorder
        )



    return render(
        request,
        'mekanik/detail_servis.html',
        {
            'workorder': workorder,
            'form': form
        }
    )