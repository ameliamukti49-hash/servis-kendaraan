from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Kendaraan, BookingServis
from .forms import KendaraanForm, BookingServisForm


# =====================================================
# DATA KENDARAAN
# =====================================================

@login_required
def kendaraan_list(request):
    kendaraan = Kendaraan.objects.filter(
        pemilik=request.user
    ).order_by("-created_at")

    return render(
        request,
        "booking/kendaraan_list.html",
        {
            "kendaraan": kendaraan
        }
    )


@login_required
def kendaraan_create(request):

    if request.method == "POST":

        form = KendaraanForm(request.POST)

        if form.is_valid():

            kendaraan = form.save(commit=False)
            kendaraan.pemilik = request.user
            kendaraan.save()

            return redirect("kendaraan_list")

    else:

        form = KendaraanForm()

    return render(
        request,
        "booking/kendaraan_form.html",
        {
            "form": form,
            "judul": "Tambah Kendaraan"
        }
    )


@login_required
def kendaraan_update(request, pk):

    kendaraan = get_object_or_404(
        Kendaraan,
        pk=pk,
        pemilik=request.user
    )

    if request.method == "POST":

        form = KendaraanForm(
            request.POST,
            instance=kendaraan
        )

        if form.is_valid():

            form.save()

            return redirect("kendaraan_list")

    else:

        form = KendaraanForm(
            instance=kendaraan
        )

    return render(
        request,
        "booking/kendaraan_form.html",
        {
            "form": form,
            "judul": "Edit Kendaraan"
        }
    )


@login_required
def kendaraan_delete(request, pk):

    kendaraan = get_object_or_404(
        Kendaraan,
        pk=pk,
        pemilik=request.user
    )

    if request.method == "POST":

        kendaraan.delete()

        return redirect("kendaraan_list")

    return render(
        request,
        "booking/kendaraan_delete.html",
        {
            "kendaraan": kendaraan
        }
    )


# =====================================================
# BOOKING SERVIS
# =====================================================

@login_required
def booking_list(request):

    booking = BookingServis.objects.filter(
        kendaraan__pemilik=request.user
    ).select_related(
        "kendaraan"
    ).order_by(
        "-tanggal_booking",
        "-jam_booking"
    )

    return render(
        request,
        "booking/booking_list.html",
        {
            "booking": booking
        }
    )
@login_required
def booking_create(request):

    if request.method == "POST":

        form = BookingServisForm(request.POST)

        form.fields["kendaraan"].queryset = Kendaraan.objects.filter(
            pemilik=request.user
        )

        if form.is_valid():

            form.save()

            return redirect("booking_list")

    else:

        form = BookingServisForm()

        form.fields["kendaraan"].queryset = Kendaraan.objects.filter(
            pemilik=request.user
        )

    return render(
        request,
        "booking/booking_form.html",
        {
            "form": form,
            "judul": "Booking Servis"
        }
    )


@login_required
def booking_update(request, pk):

    booking = get_object_or_404(
        BookingServis,
        pk=pk,
        kendaraan__pemilik=request.user
    )

    if request.method == "POST":

        form = BookingServisForm(
            request.POST,
            instance=booking
        )

        form.fields["kendaraan"].queryset = Kendaraan.objects.filter(
            pemilik=request.user
        )

        if form.is_valid():

            form.save()

            return redirect("booking_list")

    else:

        form = BookingServisForm(
            instance=booking
        )

        form.fields["kendaraan"].queryset = Kendaraan.objects.filter(
            pemilik=request.user
        )

    return render(
        request,
        "booking/booking_form.html",
        {
            "form": form,
            "judul": "Edit Booking Servis"
        }
    )


@login_required
def booking_delete(request, pk):

    booking = get_object_or_404(
        BookingServis,
        pk=pk,
        kendaraan__pemilik=request.user
    )

    if request.method == "POST":

        booking.delete()

        return redirect("booking_list")

    return render(
        request,
        "booking/booking_delete.html",
        {
            "booking": booking
        }
    )


@login_required
def booking_detail(request, pk):

    booking = get_object_or_404(
        BookingServis,
        pk=pk,
        kendaraan__pemilik=request.user
    )

    return render(
        request,
        "booking/booking_detail.html",
        {
            "booking": booking
        }
    )