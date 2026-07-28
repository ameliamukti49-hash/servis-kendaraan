from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages

# Import aman: Jika app/model teman belum ada, sistem tidak akan crash
try:
    from booking.models import BookingServis
except ImportError:
    BookingServis = None

try:
    from mekanik.models import WorkOrder
except ImportError:
    WorkOrder = None

try:
    from pembayaran.models import Pembayaran
except ImportError:
    Pembayaran = None


# Helper untuk memastikan hanya admin/staff yang bisa akses
def admin_only(user):
    return user.is_authenticated and user.is_staff


# ==========================================
# 1. DASHBOARD UTAMA & GRAFIK
# ==========================================
@user_passes_test(admin_only)
def dashboard_home(request):
    # Mengambil data summary secara aman
    total_booking = BookingServis.objects.count() if BookingServis else 0
    total_wo = WorkOrder.objects.count() if WorkOrder else 0
    
    total_omzet = 0
    if Pembayaran:
        # Menghitung total omzet dari pembayaran yang lunas
        lunas_list = Pembayaran.objects.filter(status='Lunas')
        total_omzet = sum(item.total_biaya for item in lunas_list)

    # Data Dummy untuk Grafik Bulanan (bisa disesuaikan nanti)
    grafik_bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul']
    grafik_pendapatan = [1200000, 1900000, 3000000, 5000000, 2300000, 3400000, int(total_omzet)]

    context = {
        'total_booking': total_booking,
        'total_wo': total_wo,
        'total_omzet': total_omzet,
        'grafik_bulan': grafik_bulan,
        'grafik_pendapatan': grafik_pendapatan,
    }
    return render(request, 'dashboard/index.html', context)


# ==========================================
# 2. MANAJEMEN USER (CRUD)
# ==========================================
@user_passes_test(admin_only)
def user_list(request):
    users = User.objects.all().order_by('-id')
    return render(request, 'dashboard/user_manajemen/user_list.html', {'users': users})

@user_passes_test(admin_only)
def user_create(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role') # 'admin' atau 'pelanggan'

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username sudah digunakan!')
            return redirect('dashboard:user_create')

        user = User.objects.create_user(username=username, email=email, password=password)
        if role == 'admin':
            user.is_staff = True
            user.save()
            
        messages.success(request, f'User {username} berhasil ditambahkan!')
        return redirect('dashboard:user_list')
        
    return render(request, 'dashboard/user_manajemen/user_form.html', {'aksi': 'Tambah'})

@user_passes_test(admin_only)
def user_update(request):
    # Placeholder fungsi Update untuk kelengkapan struktur routing
    messages.info(request, 'Fitur edit user siap dikembangkan.')
    return redirect('dashboard:user_list')

@user_passes_test(admin_only)
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user == request.user:
        messages.error(request, 'Anda tidak bisa menghapus akun Anda sendiri!')
    else:
        user.delete()
        messages.success(request, 'User berhasil dihapus!')
    return redirect('dashboard:user_list')


# ==========================================
# 3. MODUL LAPORAN
# ==========================================
@user_passes_test(admin_only)
def laporan_booking(request):
    tgl_mulai = request.GET.get('tgl_mulai')
    tgl_selesai = request.GET.get('tgl_selesai')
    
    bookings = BookingServis.objects.all() if BookingServis else []
    if tgl_mulai and tgl_selesai and BookingServis:
        bookings = bookings.filter(tanggal__range=[tgl_mulai, tgl_selesai])
        
    return render(request, 'dashboard/laporan/laporan_booking.html', {'bookings': bookings})

@user_passes_test(admin_only)
def laporan_servis(request):
    tgl_mulai = request.GET.get('tgl_mulai')
    tgl_selesai = request.GET.get('tgl_selesai')
    
    work_orders = WorkOrder.objects.all() if WorkOrder else []
    # Mengasumsikan field filter tanggal pengerjaan di WO bernama 'tanggal_update'
    if tgl_mulai and tgl_selesai and WorkOrder:
        work_orders = work_orders.filter(tanggal_update__range=[tgl_mulai, tgl_selesai])
        
    return render(request, 'dashboard/laporan/laporan_servis.html', {'work_orders': work_orders})

@user_passes_test(admin_only)
def laporan_pembayaran(request):
    tgl_mulai = request.GET.get('tgl_mulai')
    tgl_selesai = request.GET.get('tgl_selesai')
    
    pembayarans = Pembayaran.objects.all() if Pembayaran else []
    if tgl_mulai and tgl_selesai and Pembayaran:
        pembayarans = pembayarans.filter(tanggal_bayar__range=[tgl_mulai, tgl_selesai])
        
    total_omzet = sum(p.total_biaya for p in pembayarans) if pembayarans else 0
        
    return render(request, 'dashboard/laporan/laporan_pembayaran.html', {
        'pembayarans': pembayarans, 
        'total_omzet': total_omzet
    })


# ==========================================
# 4. CETAK PDF GLOBAL (Dinamis & Anti Eror)
# ==========================================
@user_passes_test(admin_only)
def cetak_booking_pdf(request):
    tgl_mulai = request.GET.get('tgl_mulai')
    tgl_selesai = request.GET.get('tgl_selesai')
    
    bookings = BookingServis.objects.all() if BookingServis else []
    if tgl_mulai and tgl_selesai and BookingServis:
        bookings = bookings.filter(tanggal__range=[tgl_mulai, tgl_selesai])

    headers = [
        {'nama': 'Kode', 'lebar': 15},
        {'nama': 'Pelanggan', 'lebar': 25},
        {'nama': 'Kendaraan', 'lebar': 25},
        {'nama': 'Jadwal', 'lebar': 20},
        {'nama': 'Status', 'lebar': 15}
    ]

    data_list = []
    for b in bookings:
        data_list.append({
            'kolom_data': [
                {'teks': f'#{b.id}', 'align': 'text-center', 'is_mono': True},
                {'teks': b.user.username, 'align': 'text-left', 'is_mono': False},
                {'teks': f'{b.kendaraan.merk} ({b.kendaraan.plat_nomor})', 'align': 'text-left', 'is_mono': False},
                {'teks': f'{b.tanggal}', 'align': 'text-center', 'is_mono': False},
                {'teks': b.status, 'align': 'text-center', 'is_mono': False},
            ]
        })

    context = {
        'tipe_laporan': 'Booking Servis',
        'tgl_mulai': tgl_mulai,
        'tgl_selesai': tgl_selesai,
        'tanggal_cetak': timezone.now(),
        'headers': headers,
        'data_list': data_list
    }
    return render(request, 'dashboard/laporan/pdf_template.html', context)

# Definisikan placeholder cetak lainnya agar urls.py tidak error
def cetak_servis_pdf(request): return redirect('dashboard:laporan_servis')
def cetak_pembayaran_pdf(request): return redirect('dashboard:laporan_pembayaran')