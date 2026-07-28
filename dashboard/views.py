from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone

from accounts.models import User

from booking.models import BookingServis, Kendaraan
from mekanik.models import WorkOrder
from pembayaran.models import Pembayaran

from django.contrib.auth import get_user_model
from django.contrib import messages

from django.contrib.auth.hashers import make_password
from django.db.models import Count

from django.http import HttpResponse
from reportlab.pdfgen import canvas

# =====================================================
# ROUTER DASHBOARD BERDASARKAN ROLE USER
# =====================================================

@login_required
def dashboard(request):

    role = request.user.role

    if role == "admin":
        return admin_dashboard(request)

    elif role == "service_advisor":
        return service_dashboard(request)

    elif role == "mekanik":
        return mekanik_dashboard(request)

    elif role == "kasir":
        return kasir_dashboard(request)

    elif role == "pelanggan":
        return pelanggan_dashboard(request)

    return redirect("login")


# =====================================================
# DASHBOARD ADMIN
# =====================================================

@login_required
def admin_dashboard(request):

    total_pelanggan = User.objects.filter(
        role="pelanggan"
    ).count()

    total_kendaraan = Kendaraan.objects.count()

    total_booking = BookingServis.objects.count()

    total_workorder = WorkOrder.objects.count()

    total_pembayaran = Pembayaran.objects.count()


    total_pendapatan = (
        Pembayaran.objects.aggregate(
            total=Sum("total_bayar")
        )["total"] or 0
    )


    booking_terbaru = BookingServis.objects.order_by(
        "-id"
    )[:5]


    workorder_terbaru = WorkOrder.objects.order_by(
        "-id"
    )[:5]


    context = {

        "title": "Dashboard Admin",

        "total_pelanggan": total_pelanggan,

        "total_kendaraan": total_kendaraan,

        "total_booking": total_booking,

        "total_workorder": total_workorder,

        "total_pembayaran": total_pembayaran,

        "total_pendapatan": total_pendapatan,

        "booking_terbaru": booking_terbaru,

        "workorder_terbaru": workorder_terbaru,

    }


    return render(
        request,
        "dashboard/admin_dashboard.html",
        context
    )



# =====================================================
# DASHBOARD SERVICE ADVISOR
# =====================================================

@login_required
def service_dashboard(request):

    hari_ini = timezone.now().date()


    booking_hari_ini = BookingServis.objects.filter(
        tanggal_booking=hari_ini
    ).count()


    booking_menunggu = BookingServis.objects.filter(
        status="menunggu"
    ).count()


    booking_diproses = BookingServis.objects.filter(
        status="diproses"
    ).count()


    daftar_booking = BookingServis.objects.order_by(
        "-id"
    )[:10]


    context = {

        "title": "Dashboard Service Advisor",

        "booking_hari_ini": booking_hari_ini,

        "booking_menunggu": booking_menunggu,

        "booking_diproses": booking_diproses,

        "daftar_booking": daftar_booking,

    }


    return render(
        request,
        "dashboard/service_dashboard.html",
        context
    )



# =====================================================
# DASHBOARD MEKANIK
# =====================================================

@login_required
def mekanik_dashboard(request):


    total_workorder = WorkOrder.objects.count()


    workorder_proses = WorkOrder.objects.filter(
        status="diproses"
    ).count()


    workorder_selesai = WorkOrder.objects.filter(
        status="selesai"
    ).count()


    daftar_workorder = WorkOrder.objects.order_by(
        "-id"
    )[:10]


    context = {

        "title": "Dashboard Mekanik",

        "total_workorder": total_workorder,

        "workorder_proses": workorder_proses,

        "workorder_selesai": workorder_selesai,

        "daftar_workorder": daftar_workorder,

    }


    return render(
        request,
        "dashboard/mekanik_dashboard.html",
        context
    )



# =====================================================
# DASHBOARD KASIR
# =====================================================

@login_required
def kasir_dashboard(request):


    total_transaksi = Pembayaran.objects.count()


    total_pendapatan = (
        Pembayaran.objects.aggregate(
            total=Sum("total_bayar")
        )["total"] or 0
    )


    pembayaran_terbaru = Pembayaran.objects.order_by(
        "-id"
    )[:10]


    context = {

        "title": "Dashboard Kasir",

        "total_transaksi": total_transaksi,

        "total_pendapatan": total_pendapatan,

        "pembayaran_terbaru": pembayaran_terbaru,

    }


    return render(
        request,
        "dashboard/kasir_dashboard.html",
        context
    )



# =====================================================
# DASHBOARD PELANGGAN
# =====================================================

@login_required
def pelanggan_dashboard(request):


    booking_saya = BookingServis.objects.filter(
        kendaraan__pemilik=request.user
    ).order_by(
        "-id"
    )


    total_booking = booking_saya.count()


    context = {

        "title": "Dashboard Pelanggan",

        "booking_saya": booking_saya,

        "total_booking": total_booking,

    }


    return render(
        request,
        "dashboard/pelanggan_dashboard.html",
        context
    )
    
# =====================================================
# MANAJEMEN USER ADMIN
# =====================================================

User = get_user_model()


@login_required
def user_list(request):

    if request.user.role != "admin":
        return redirect("dashboard")


    users = User.objects.all().order_by("-id")


    context = {
        "title": "Manajemen User",
        "users": users
    }


    return render(
        request,
        "dashboard/user_list.html",
        context
    )



@login_required
def user_delete(request, id):

    if request.user.role != "admin":
        return redirect("dashboard")


    user = User.objects.get(id=id)


    if user != request.user:

        user.delete()

        messages.success(
            request,
            "User berhasil dihapus"
        )


    return redirect(
        "dashboard:user_list"
    )
    
# =====================================================
# TAMBAH USER ADMIN
# =====================================================

@login_required
def user_create(request):

    if request.user.role != "admin":
        return redirect("dashboard")


    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")


        User.objects.create(
            username=username,
            email=email,
            password=make_password(password),
            role=role
        )


        return redirect(
            "dashboard:user_list"
        )


    return render(
        request,
        "dashboard/user_form.html"
    )

@login_required
def user_edit(request, id):

    if request.user.role != "admin":
        return redirect("dashboard")


    user = User.objects.get(id=id)


    if request.method == "POST":

        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.role = request.POST.get("role")

        user.save()


        return redirect(
            "dashboard:user_list"
        )


    return render(
        request,
        "dashboard/user_edit.html",
        {
            "user": user
        }
    )
    
# =====================================================
# LAPORAN ADMIN
# =====================================================

@login_required
def laporan(request):

    if request.user.role != "admin":
        return redirect("dashboard")


    total_booking = BookingServis.objects.count()

    total_servis = WorkOrder.objects.count()

    total_pembayaran = Pembayaran.objects.count()


    booking_data = BookingServis.objects.all().order_by(
        "-tanggal_booking"
    )


    servis_data = WorkOrder.objects.all().order_by(
        "-tanggal_mulai"
    )


    pembayaran_data = Pembayaran.objects.all().order_by(
        "-tanggal_bayar"
    )


    context = {

        "title": "Laporan",

        "total_booking": total_booking,

        "total_servis": total_servis,

        "total_pembayaran": total_pembayaran,


        "booking_data": booking_data,

        "servis_data": servis_data,

        "pembayaran_data": pembayaran_data,

    }


    return render(
        request,
        "dashboard/laporan.html",
        context
    )
    
# =====================================================
# GRAFIK DASHBOARD
# =====================================================

@login_required
def grafik(request):

    if request.user.role != "admin":
        return redirect("dashboard")


    status_booking = (
        BookingServis.objects
        .values("status")
        .annotate(
            jumlah=Count("id")
        )
    )


    label_booking = []
    data_booking = []


    for item in status_booking:

        label_booking.append(
            item["status"]
        )

        data_booking.append(
            item["jumlah"]
        )



    pembayaran = (
        Pembayaran.objects
        .values("metode")
        .annotate(
            jumlah=Count("id")
        )
    )


    label_pembayaran = []
    data_pembayaran = []


    for item in pembayaran:

        label_pembayaran.append(
            item["metode"]
        )

        data_pembayaran.append(
            item["jumlah"]
        )



    context = {

        "label_booking": label_booking,

        "data_booking": data_booking,

        "label_pembayaran": label_pembayaran,

        "data_pembayaran": data_pembayaran,

    }


    return render(
        request,
        "dashboard/grafik.html",
        context
    )
    
# =====================================================
# CETAK PDF LAPORAN
# =====================================================

@login_required
def cetak_pdf(request):

    if request.user.role != "admin":
        return redirect("dashboard")


    response = HttpResponse(
        content_type="application/pdf"
    )

    response[
        "Content-Disposition"
    ] = "attachment; filename=laporan_bengkel.pdf"


    pdf = canvas.Canvas(response)


    pdf.setTitle(
        "Laporan Bengkel"
    )


    y = 800


    pdf.setFont(
        "Helvetica-Bold",
        16
    )

    pdf.drawString(
        50,
        y,
        "LAPORAN SERVIS BENGKEL"
    )


    y -= 40


    pdf.setFont(
        "Helvetica",
        11
    )


    total_booking = BookingServis.objects.count()

    total_servis = WorkOrder.objects.count()

    total_bayar = Pembayaran.objects.count()



    data = [

        f"Total Booking : {total_booking}",

        f"Total Work Order : {total_servis}",

        f"Total Pembayaran : {total_bayar}",

    ]


    for item in data:

        pdf.drawString(
            50,
            y,
            item
        )

        y -= 25



    y -= 20


    pdf.drawString(
        50,
        y,
        "Daftar Booking:"
    )


    y -= 25



    booking = BookingServis.objects.all()[:10]


    for b in booking:

        text = (
            f"{b.kendaraan.nomor_polisi} - "
            f"{b.status}"
        )


        pdf.drawString(
            60,
            y,
            text
        )


        y -= 20


        if y < 50:

            pdf.showPage()

            y = 800



    pdf.save()


    return response