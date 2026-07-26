from django.shortcuts import render


def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')


def pelanggan_dashboard(request):
    return render(request, 'dashboard/pelanggan_dashboard.html')


def mekanik_dashboard(request):
    return render(request, 'dashboard/mekanik_dashboard.html')


def kasir_dashboard(request):
    return render(request, 'dashboard/kasir_dashboard.html')