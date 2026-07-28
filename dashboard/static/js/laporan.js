/* static/js/laporan.js */
document.addEventListener("DOMContentLoaded", function () {
    
    // Fungsi inisialisasi DataTables dengan tombol ekspor kustom
    function initDataTable(tableSelector, titleText) {
        if ($.fn.DataTable.isDataTable(tableSelector)) return;

        $(tableSelector).DataTable({
            responsive: true,
            pageLength: 10,
            dom: "<'row mb-3'<'col-md-7'B><'col-md-5'f>>" +
                 "<'row'<'col-12'tr>>" +
                 "<'row mt-3'<'col-md-5'i><'col-md-7 d-flex justify-content-md-end'p>>",
            buttons: [
                {
                    extend: 'excelHtml5',
                    title: titleText,
                    className: 'btn buttons-excel',
                    text: '<i class="bi bi-file-earmark-spreadsheet me-2"></i>Unduh Excel'
                },
                {
                    extend: 'pdfHtml5',
                    title: titleText,
                    className: 'btn buttons-pdf',
                    text: '<i class="bi bi-file-earmark-pdf me-2"></i>Ekspor PDF',
                    orientation: 'landscape',
                    pageSize: 'A4'
                },
                {
                    extend: 'print',
                    title: titleText,
                    className: 'btn buttons-print',
                    text: '<i class="bi bi-printer me-2"></i>Cetak Dokumen'
                }
            ],
            language: {
                search: "_INPUT_",
                searchPlaceholder: "Cari lembar laporan...",
                lengthMenu: "Tampilkan _MENU_ entri data",
                paginate: {
                    previous: "<i class='bi bi-chevron-left'></i>",
                    next: "<i class='bi bi-chevron-right'></i>"
                }
            }
        });
    }

    // Inisialisasi default pada Tab Pertama yang aktif (Laporan Booking)
    initDataTable('#tabBooking table', 'Laporan Rekapitulasi Booking BengkelKu');

    // Trigger inisialisasi DataTables saat tab lain diklik pengguna (Lazy Load Engine)
    $('button[data-bs-toggle="tab"]').on('shown.bs.tab', function (e) {
        let targetId = $(e.target).data('bs-target');
        let table = $(targetId).find('table');
        let title = $(e.target).text().trim();
        initDataTable(table, `Dokumen ${title} - BengkelKu`);
    });

    // SISTEM FILTER INPUT CROSS-DATATABLES HANDLER
    $('#filterStatus, #filterMekanik, #filterJenisServis').on('change', function() {
        let activeTable = $('.tab-pane.active').find('table').DataTable();
        let searchVal = $(this).val();
        
        // Melakukan global search berdasarkan nilai filter kontrol
        activeTable.search(searchVal).draw();
    });

    $('#filterTanggal').on('change', function() {
        let activeTable = $('.tab-pane.active').find('table').DataTable();
        activeTable.column(1).search($(this).val()).draw();
    });
});