/* static/js/grafik.js */
document.addEventListener("DOMContentLoaded", function () {

    // Token Warna Blue Premium Design System
    const colors = {
        primary: '#2563EB',
        secondary: '#3B82F6',
        accent: '#60A5FA',
        softBlue: '#DBEAFE',
        success: '#22C55E',
        warning: '#F59E0B',
        danger: '#EF4444',
        textPrimary: '#1E293B',
        textSecondary: '#64748B'
    };

    // Konfigurasi Font Global Chart.js
    Chart.defaults.font.family = 'Poppins';
    Chart.defaults.font.size = 12;
    Chart.defaults.color = colors.textSecondary;

    // 1. CHART BOOKING BULANAN (Bar Chart)
    new Chart(document.getElementById('chartBookingBulanan'), {
        type: 'bar',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'],
            datasets: [{
                label: 'Total Booking',
                data: [120, 145, 132, 168, 190, 210, 185, 198, 220, 240, 215, 260],
                backgroundColor: colors.secondary,
                borderRadius: 8,
                hoverBackgroundColor: colors.primary
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { grid: { display: false } },
                y: { grid: { color: '#F1F5F9' }, border: { dash: [5, 5] } }
            }
        }
    });

    // 2. CHART STATUS BOOKING (Doughnut Chart)
    new Chart(document.getElementById('chartStatusBooking'), {
        type: 'doughnut',
        data: {
            labels: ['Selesai', 'Diproses', 'Reschedule', 'Batal'],
            datasets: [{
                data: [65, 20, 10, 5],
                backgroundColor: [colors.success, colors.secondary, colors.warning, colors.danger],
                borderWidth: 2,
                hoverOffset: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'bottom', labels: { usePointStyle: true } }
            }
        }
    });

    // 3. CHART PENDAPATAN BULANAN (Line Chart dengan Area Fill)
    new Chart(document.getElementById('chartPendapatan'), {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul'],
            datasets: [{
                label: 'Omset Karyawan (Rp)',
                data: [35000000, 42000000, 39000000, 51000000, 68000000, 62000000, 75000000],
                borderColor: colors.primary,
                backgroundColor: 'rgba(59, 130, 246, 0.08)',
                fill: true,
                tension: 0.3,
                borderWidth: 3,
                pointBackgroundColor: colors.primary
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                y: { ticks: { callback: value => 'Rp ' + value.toLocaleString('id-ID') } }
            }
        }
    });

    // 4. CHART JENIS SERVIS (Polar Area Chart)
    new Chart(document.getElementById('chartJenisServis'), {
        type: 'polarArea',
        data: {
            labels: ['Servis Ringan', 'Tune Up', 'Ganti Oli', 'Overhaul', 'Kelistrikan'],
            datasets: [{
                data: [40, 25, 55, 12, 18],
                backgroundColor: [
                    'rgba(37, 99, 235, 0.7)',
                    'rgba(96, 165, 250, 0.7)',
                    'rgba(34, 197, 94, 0.7)',
                    'rgba(239, 68, 68, 0.7)',
                    'rgba(245, 158, 11, 0.7)'
                ]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'bottom' } }
        }
    });

    // 5. CHART TOP MEKANIK (Horizontal Bar Chart)
    new Chart(document.getElementById('chartTopMekanik'), {
        type: 'bar',
        data: {
            labels: ['Agus D.', 'Rian H.', 'Bambang U.', 'Hendra S.', 'Deddy K.'],
            datasets: [{
                data: [84, 76, 71, 65, 58],
                backgroundColor: colors.accent,
                borderRadius: 6,
                hoverBackgroundColor: colors.primary
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } }
        }
    });

    // 6. CHART TOP SPAREPART (Radar Chart)
    new Chart(document.getElementById('chartTopSparepart'), {
        type: 'radar',
        data: {
            labels: ['Oli Mesin', 'Kampas Rem', 'Filter Udara', 'Busi', 'Aki Motor/Mobil'],
            datasets: [{
                label: 'Unit Terjual',
                data: [180, 140, 125, 160, 95],
                borderColor: colors.primary,
                backgroundColor: 'rgba(37, 99, 235, 0.2)',
                pointBackgroundColor: colors.primary
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
});