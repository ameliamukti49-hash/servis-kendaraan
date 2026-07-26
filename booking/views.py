from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Kendaraan, BookingServis
from .forms import KendaraanForm, BookingServisForm


# ==========================
# DATA KENDARAAN
# ==========================

@login_required
def kendaraan_list(request):

    kendaraan = Kendaraan.objects.filter(
        pemilik=request.user
    ).order_by('-created_at')

    context = {
        'kendaraan': kendaraan
    }

    return render(
        request,
        'booking/kendaraan_list.html',
        context
    )


@login_required
def kendaraan_create(request):

    if request.method == 'POST':

        form = KendaraanForm(request.POST)

        if form.is_valid():

            data = form.save(commit=False)

            data.pemilik = request.user

            data.save()

            return redirect('kendaraan_list')

    else:

        form = KendaraanForm()

    context = {
        'form': form,
        'judul': 'Tambah Kendaraan'
    }

    return render(
        request,
        'booking/kendaraan_form.html',
        context
    )


@login_required
def kendaraan_update(request, pk):

    kendaraan = get_object_or_404(
        Kendaraan,
        pk=pk,
        pemilik=request.user
    )

    if request.method == 'POST':

        form = KendaraanForm(
            request.POST,
            instance=kendaraan
        )

        if form.is_valid():

            form.save()

            return redirect('kendaraan_list')

    else:

        form = KendaraanForm(
            instance=kendaraan
        )

    context = {

        'form': form,

        'judul': 'Edit Kendaraan'

    }

    return render(

        request,

        'booking/kendaraan_form.html',

        context

    )
    @login_required
    def kendaraan_delete(request, pk):

        kendaraan = get_object_or_404(
        Kendaraan,
        pk=pk,
        pemilik=request.user
    )

    if request.method == 'POST':

        kendaraan.delete()

        return redirect('kendaraan_list')

    context = {

        'kendaraan': kendaraan

    }

    return render(

        request,

        'booking/kendaraan_delete.html',

        context

    )


# ==========================
# BOOKING SERVIS
# ==========================

@login_required
def booking_list(request):

    booking = BookingServis.objects.filter(
        kendaraan__pemilik=request.user
    ).select_related(
        'kendaraan'
    ).order_by(
        '-tanggal_booking',
        '-jam_booking'
    )

    context = {

        'booking': booking

    }

    return render(

        request,

        'booking/booking_list.html',

        context

    )


@login_required
def booking_create(request):

    if request.method == 'POST':

        form = BookingServisForm(request.POST)

        form.fields['kendaraan'].queryset = Kendaraan.objects.filter(
            pemilik=request.user
        )

        if form.is_valid():

            form.save()

            return redirect('booking_list')

    else:

        form = BookingServisForm()

        form.fields['kendaraan'].queryset = Kendaraan.objects.filter(
            pemilik=request.user
        )

    context = {

        'form': form,

        'judul': 'Booking Servis'

    }

    return render(

        request,

        'booking/booking_form.html',

        context

    )


@login_required
def booking_update(request, pk):

    booking = get_object_or_404(
        BookingServis,
        pk=pk,
        kendaraan__pemilik=request.user
    )

    if request.method == 'POST':

        form = BookingServisForm(
            request.POST,
            instance=booking
        )

        form.fields['kendaraan'].queryset = Kendaraan.objects.filter(
            pemilik=request.user
        )

        if form.is_valid():

            form.save()

            return redirect('booking_list')

    else:

        form = BookingServisForm(
            instance=booking
        )

        form.fields['kendaraan'].queryset = Kendaraan.objects.filter(
            pemilik=request.user
        )

    context = {

        'form': form,

        'judul': 'Edit Booking Servis'

    }

    return render(

        request,

        'booking/booking_form.html',

        context

    )
    @login_required
    def booking_delete(request, pk):

        booking = get_object_or_404(
        BookingServis,
        pk=pk,
        kendaraan__pemilik=request.user
    )

    if request.method == 'POST':

        booking.delete()

        return redirect('booking_list')

    context = {

        'booking': booking

    }

    return render(

        request,

        'booking/booking_delete.html',

        context

    )


@login_required
def booking_detail(request, pk):

    booking = get_object_or_404(

        BookingServis,

        pk=pk,

        kendaraan__pemilik=request.user

    )

    context = {

        'booking': booking

    }

    return render(

        request,

        'booking/booking_detail.html',

        context

    )