/* dashboard/static/js/dashboard.js */
document.addEventListener("DOMContentLoaded", function () {
    // 1. Inisialisasi Counter Statistik Teranimasi
    const animatedCounters = document.querySelectorAll('.saas-counter');
    animatedCounters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        const count = 0;
        const speed = target / 40; 
        
        const updateCount = () => {
            const current = +counter.innerText.replace(/[^0-9]/g, '');
            if(current < target) {
                const nextValue = Math.ceil(current + speed);
                counter.innerText = target > 5000 ? "Rp " + nextValue.toLocaleString('id-ID') : nextValue;
                setTimeout(updateCount, 16);
            } else {
                counter.innerText = target > 5000 ? "Rp " + target.toLocaleString('id-ID') : target;
            }
        };
        updateCount();
    });

    // 2. Inisialisasi Chart Premium Minimalis
    const chartCtx = document.getElementById('saasChartPerformance');
    if (chartCtx) {
        new Chart(chartCtx, {
            type: 'line',
            data: {
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                datasets: [{
                    data: [14, 22, 19, 35, 28, 44, 30],
                    borderColor: '#2563EB',
                    borderWidth: 2.5,
                    pointRadius: 0,
                    pointHoverRadius: 6,
                    tension: 0.38,
                    fill: true,
                    backgroundColor: 'rgba(37, 99, 235, 0.03)'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: {
                    x: { grid: { display: false }, ticks: { font: { family: 'Poppins' } } },
                    y: { grid: { color: 'rgba(226, 232, 240, 0.3)' }, border: { dash: [4, 4] } }
                }
            }
        });
    }
});