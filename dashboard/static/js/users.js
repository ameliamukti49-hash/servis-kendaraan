/* static/js/users.js */
document.addEventListener("DOMContentLoaded", function () {
    
    // 1. Inisialisasi DataTables Enterprise Teroptimasi & Responsive
    let table = $('#tableMasterUsers').DataTable({
        responsive: true,
        pageLength: 10,
        dom: "<'row mb-3'<'col-md-6'l><'col-md-6 d-flex justify-content-md-end'f>>" +
             "<'row'<'col-12'tr>>" +
             "<'row mt-3'<'col-md-5'i><'col-md-7 d-flex justify-content-md-end'p>>",
        language: {
            search: "_INPUT_",
            searchPlaceholder: "Cari karyawan, role, email...",
            lengthMenu: "Tampilkan _MENU_ entri data",
            info: "Menampilkan _START_ sampai _END_ dari _TOTAL_ user",
            paginate: {
                previous: "<i class='bi bi-chevron-left'></i>",
                next: "<i class='bi bi-chevron-right'></i>"
            }
        }
    });

    // 2. Custom Role Filter Trigger (Dapat disematkan pada tombol luar DataTables)
    $('.role-filter-btn').on('click', function() {
        let val = $(this).data('role');
        table.column(3).search(val).draw();
    });

    // 3. SweetAlert2 Ajax Engine: Prosedur Penghapusan User Aman
    $(document).on('click', '.btn-delete-user', function() {
        const userId = $(this).data('id');
        const username = $(this).data('name');
        
        // Ambil CSRF Token bawaan Django dari form modal
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        Swal.fire({
            title: `Hapus User @${username}?`,
            text: "Tindakan ini permanen dan akan memutuskan seluruh log kerja operasional user terkait!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#EF4444', // Danger color code token
            cancelButtonColor: '#64748B',  // Secondary color code token
            confirmButtonText: 'Ya, Hapus Akun',
            cancelButtonText: 'Batal',
            focusCancel: true
        }).then((result) => {
            if (result.isConfirmed) {
                // Trigger fetch API AJAX untuk penghapusan
                fetch(`/dashboard/users/delete/${userId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        Swal.fire({
                            title: 'Terhapus!',
                            text: data.message,
                            icon: 'success',
                            timer: 2000,
                            showConfirmButton: false
                        }).then(() => {
                            location.reload(); // Reload halaman untuk sync database state
                        });
                    } else {
                        Swal.fire({
                            title: 'Gagal Sistem',
                            text: data.message,
                            icon: 'error'
                        });
                    }
                })
                .catch(error => {
                    Swal.fire({
                        title: 'Error Koneksi',
                        text: 'Terjadi pemutusan komunikasi AJAX dengan backend Django.',
                        icon: 'error'
                    });
                });
            }
        });
    });
});