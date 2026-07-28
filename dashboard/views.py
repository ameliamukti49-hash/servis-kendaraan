# dashboard/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from datetime import timedelta

# Import Form & Model Internal (Akan dibuat di folder dashboard kamu sendiri)
from .models import UserProfile
from .forms import UserMasterForm, UserProfileForm
import os
import io
import base64
import qrcode
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from weasyprint import HTML, CSS
# dashboard/views.py
from django.db import transaction  # PENTING: Untuk mengamankan database transaction
from django.core.exceptions import PermissionDenied  # PENTING: Untuk proteksi hak akses

@login_required
def user_create_view(request):
    """
    [OPTIMIZED] API Endpoint Create User Baru dengan Proteksi ACID Transaction.
    Menjamin User & Profile tersimpan bersamaan. Jika salah satu gagal, database otomatis di-rollback.
    """
    if not request.user.groups.filter(name='Admin').exists() and not request.user.is_superuser:
        messages.error(request, 'Anda tidak memiliki otoritas eksekusi.')
        return redirect('dashboard:user_list')

    if request.method == 'POST':
        u_form = UserMasterForm(request.POST)
        p_form = UserProfileForm(request.POST, request.FILES)
        
        if u_form.is_valid() and p_form.is_valid():
            try:
                # Menggunakan decorator atomic untuk menjamin keamanan operasi database
                with transaction.atomic():
                    user = u_form.save(commit=False)
                    if u_form.cleaned_data.get('password'):
                        user.set_password(u_form.cleaned_data.get('password'))
                    else:
                        user.set_password('bengkelku123')
                    user.save()
                    
                    profile = p_form.save(commit=False)
                    profile.user = user
                    profile.save()
                
                messages.success(request, f'Akun @{user.username} berhasil didaftarkan secara aman.')
                return redirect('dashboard:user_list')
            except Exception as e:
                messages.error(request, f'Gagal mengamankan transaksi data: {str(e)}')
        else:
            messages.error(request, 'Data form tidak valid. Periksa kembali format inputan Anda.')
            
    return redirect('dashboard:user_list')


@login_required
def export_invoice_pdf(request, invoice_id="INV-9021"):
    """
    [OPTIMIZED] Engine Ekspor PDF WeasyPrint dengan Proteksi Keamanan Tingkat Tinggi (Anti-IDOR).
    Mencegah mekanik/user non-authorized mengintip dokumen invoice keuangan secara ilegal.
    """
    # 1. VALIDASI KEAMANAN: Batasi hanya Admin dan Kasir yang boleh mencetak dokumen keuangan
    is_admin = request.user.groups.filter(name='Admin').exists() or request.user.is_superuser
    is_kasir = request.user.groups.filter(name='Kasir').exists()
    
    if not (is_admin or is_kasir):
        # Tolak akses secara rigid dengan melemparkan HTTP 403 Forbidden
        raise PermissionDenied("Akses ditolak. Anda tidak memiliki izin mencetak dokumen finansial.")

    # 2. PENGAMBILAN DATA (Gunakan select_related jika data ditarik dari DB asli milik rekan terkait)
    # invoice = get_object_or_404(Invoice.objects.select_related('customer', 'vehicle'), nomor=invoice_id)
    
    # Mockup data representatif struktural
    context = {
        'invoice_id': invoice_id,
        'tanggal': timezone.now().strftime('%d %B %Y'),
        'pelanggan': 'Ahmad Fauzi',
        'unit': 'Toyota Avanza (B 1234 XY)',
        'mekanik': 'Agus Darmawan',
        'admin_name': request.user.get_full_name() or request.user.username,
        'items': [
            {'desc': 'Jasa Servis Berkala / Tune Up', 'qty': 1, 'price': 150000, 'sub': 150000},
            {'desc': 'Oli Mesin Shell Helix Ultra 4L', 'qty': 1, 'price': 450000, 'sub': 450000},
            {'desc': 'Kampas Rem Depan Genuine', 'qty': 1, 'price': 250000, 'sub': 250000},
        ],
        'total': 850000
    }

    # 3. GENERATE VALIDATION QR CODE
    qr_data = f"https://bengkelku.id/verify/invoice/{invoice_id}"
    qr = qrcode.QRCode(version=1, box_size=10, border=0)
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    img_buf = io.BytesIO()
    qr_img = qr.make_image(fill_color="#1E293B", back_color="white")
    qr_img.save(img_buf, format="PNG")
    qr_base64 = base64.b64encode(img_buf.getvalue()).decode('utf-8')
    context['qr_code_base64'] = qr_base64

    # 4. WEASYPRINT RENDERING ENGINE VIA MEMORY BUFFER
    try:
        html_string = render_to_string('pdf/pdf.html', context)
        html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
        pdf_file = html.write_pdf()

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="Invoice_{invoice_id}.pdf"'
        return response
    except Exception as e:
        return HttpResponse(f"Gagal memproses pembuatan PDF: {str(e)}", status=500)


# =========================================================================
# CORE 1: ROUTER DASHBOARD LINTAS ROLE
# =========================================================================
# dashboard/views.py

class DashboardRoutingView(LoginRequiredMixin, TemplateView):
    """
    Arsitektur Router Dashboard BengkelKu Teroptimasi.
    Menarik data agregasi lintas modul secara aman dengan sistem deteksi Role
    agar sidebar berubah secara dinamis tanpa merusak struktur file tim lain.
    """
    
    def get(self, request, *args, **kwargs):
        user = request.user
        context = self.get_dashboard_metrics() # Menggunakan fungsi metrics bawaanmu yang sudah ada
        
        # 1. Deteksi Role Berdasarkan Group Django
        if user.is_superuser or user.groups.filter(name='Admin').exists():
            context['current_role'] = 'Admin'
            return render(request, 'dashboard/dashboard_admin.html', context)
        elif user.groups.filter(name='Service Advisor').exists():
            context['current_role'] = 'Service Advisor'
            return render(request, 'dashboard/dashboard_service.html', context)
        elif user.groups.filter(name='Mekanik').exists():
            context['current_role'] = 'Mekanik'
            return render(request, 'dashboard/dashboard_mekanik.html', context)
        elif user.groups.filter(name='Kasir').exists():
            context['current_role'] = 'Kasir'
            return render(request, 'dashboard/dashboard_kasir.html', context)
        
        # Fallback jika user baru didaftarkan belum masuk group
        context['current_role'] = 'Admin' 
        return render(request, 'dashboard/dashboard_admin.html', context)

    def get_dashboard_metrics(self):
        today = timezone.now().date()
        
        # 1. Fallback & Integrasi Ambil Data ORM untuk Modul Booking (Milik Anggota Terkait)[cite: 2]
        if Booking:
            booking_hari_ini = Booking.objects.filter(tanggal_booking=today).count()
            total_pelanggan = Booking.objects.values('pelanggan_id').distinct().count()
            recent_bookings = Booking.objects.order_selection('-created_at')[:5]
        else:
            booking_hari_ini = 18  # Mockup data representatif industri jika belum di-merge[cite: 2]
            total_pelanggan = 1420[cite: 2]
            recent_bookings = [
                {'id': 'BK-1029', 'nama': 'Ahmad Fauzi', 'unit': 'Toyota Avanza', 'waktu': '09:00', 'status': 'Dikonfirmasi'},
                {'id': 'BK-1030', 'nama': 'Siti Aminah', 'unit': 'Honda HR-V', 'waktu': '10:30', 'status': 'Pending'},
                {'id': 'BK-1031', 'nama': 'Budi Sudarsono', 'unit': 'Mitsubishi Xpander', 'waktu': '11:15', 'status': 'Dikonfirmasi'},
            ]

        # 2. Fallback & Integrasi Ambil Data ORM untuk Modul Kerja Mekanik (Milik Anggota Terkait)[cite: 2]
        if WorkOrder:
            servis_hari_ini = WorkOrder.objects.filter(tanggal_kerja=today, status='Selesai').count()
            recent_work_orders = WorkOrder.objects.filter(status='Proses')[:5]
        else:
            servis_hari_ini = 24[cite: 2]
            recent_work_orders = [
                {'id': 'WO-8821', 'mekanik': 'Agus Darmawan', 'unit': 'Suzuki Ertiga', 'progres': 75, 'status': 'Perbaikan Mesin'},
                {'id': 'WO-8822', 'mekanik': 'Rian Hidayat', 'unit': 'Honda Vario', 'progres': 40, 'status': 'Servis Berkala'},
                {'id': 'WO-8823', 'mekanik': 'Bambang U.', 'unit': 'Daihatsu Terios', 'progres': 90, 'status': 'Spooring Balancing'},
            ]

        # 3. Fallback & Integrasi Ambil Data ORM untuk Modul Keuangan (Milik Anggota Terkait)[cite: 2]
        if Invoice:
            from django.db.models import Sum
            pendapatan = Invoice.objects.filter(tanggal_bayar=today, status='Lunas').aggregate(Sum('total'))['total__sum'] or 0
        else:
            pendapatan = 4850000[cite: 2]

        return {
            'page_title': 'Dashboard System',
            'booking_hari_ini': booking_hari_ini,
            'servis_hari_ini': servis_hari_ini,
            'pendapatan': pendapatan,
            'total_pelanggan': total_pelanggan,
            'recent_bookings': recent_bookings,
            'recent_work_orders': recent_work_orders,
            'current_date': today.strftime('%B %Y')
        }

# =========================================================================
# CORE 2: ENTERPRISE USER MANAGEMENT LOGIC (CRUD & SECURITY)
# =========================================================================
@login_required
def user_list_view(request):
    """ Menampilkan halaman master user data dengan DataTables & Modal """
    if not request.user.groups.filter(name='Admin').exists() and not request.user.is_superuser:
        messages.error(request, 'Anda tidak memiliki hak akses manajemen user.')
        return redirect('dashboard:index')

    users = User.objects.select_related('profile').all().order_by('-date_joined')
    u_form = UserMasterForm()
    p_form = UserProfileForm()

    context = {
        'page_title': 'Manajemen User BengkelKu',
        'users': users,
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/user_list.html', context)


@login_required
def user_delete_view(request, user_id):
    """ AJAX Safe Deletion Engine dengan Restriksi Self-Deletion """
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        if user == request.user:
            return JsonResponse({'status': 'error', 'message': 'Dilarang menghapus akun sendiri yang sedang aktif!'})
        
        username = user.username
        user.delete()
        return JsonResponse({'status': 'success', 'message': f'Akun {username} sukses dihapus permanent.'})
    return JsonResponse({'status': 'error', 'message': 'Metode request tidak valid'})

@login_required
def grafik_view(request):
    """ Mengagregasikan data statistik performa bengkel """
    # Data dikondisikan siap menerima parameter filter (request.GET.get('bulan'), dll)
    context = {
        'page_title': 'Statistik & Analisis BengkelKu',
        'tahun_list': [2024, 2025, 2026],
        'bulan_list': [
            {'num': 1, 'name': 'Januari'}, {'num': 2, 'name': 'Februari'},
            {'num': 3, 'name': 'Maret'}, {'num': 4, 'name': 'April'},
            {'num': 5, 'name': 'Mei'}, {'num': 6, 'name': 'Juni'},
            {'num': 7, 'name': 'Juli'}, {'num': 8, 'name': 'Agustus'},
            {'num': 9, 'name': 'September'}, {'num': 10, 'name': 'Oktober'},
            {'num': 11, 'name': 'November'}, {'num': 12, 'name': 'Desember'}
        ]
    }
    return render(request, 'grafik/grafik.html', context)

@login_required
def laporan_view(request):
    """ View Kontroler Laporan Terpadu Lintas Modul """
    # Mockup Data untuk dropdown filter
    list_mekanik = ['Agus Darmawan', 'Rian Hidayat', 'Bambang U.', 'Hendra S.']
    list_jenis_servis = ['Servis Ringan', 'Tune Up', 'Ganti Oli', 'Overhaul', 'Kelistrikan']
    
    context = {
        'page_title': 'Laporan Terpadu BengkelKu',
        'list_mekanik': list_mekanik,
        'list_jenis_servis': list_jenis_servis,
        # Contoh data dummy terstruktur yang akan dibaca oleh DataTables
        'report_data': {
            'booking': [
                {'id': 'BK-001', 'tgl': '2026-07-25', 'nama': 'Ahmad Fauzi', 'unit': 'Toyota Avanza', 'status': 'Selesai', 'mekanik': 'Agus Darmawan', 'tipe': 'Tune Up'},
                {'id': 'BK-002', 'tgl': '2026-07-26', 'nama': 'Siti Aminah', 'unit': 'Honda HR-V', 'status': 'Diproses', 'mekanik': 'Rian Hidayat', 'tipe': 'Ganti Oli'},
            ],
            'pendapatan': [
                {'inv': 'INV-9021', 'tgl': '2026-07-25', 'nama': 'Ahmad Fauzi', 'tipe': 'Tune Up', 'total': 450000, 'status': 'Lunas'},
                {'inv': 'INV-9022', 'tgl': '2026-07-26', 'nama': 'Siti Aminah', 'tipe': 'Ganti Oli', 'total': 150000, 'status': 'Lunas'},
            ],
            'sparepart': [
                {'kode': 'SP-Oli-01', 'nama': 'Oli Mesin Shell Helix', 'kategori': 'Pelumas', 'terjual': 45, 'stok': 12, 'total': 5400000},
                {'kode': 'SP-Brd-02', 'nama': 'Kampas Rem Depan Avanza', 'kategori': 'Braking', 'terjual': 20, 'stok': 8, 'total': 3000000},
            ]
        }
    }
    return render(request, 'laporan/laporan.html', context)