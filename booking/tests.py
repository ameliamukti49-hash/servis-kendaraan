from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Kendaraan, BookingServis


User = get_user_model()


class KendaraanModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345678'
        )

    def test_create_kendaraan(self):
        kendaraan = Kendaraan.objects.create(
            pemilik=self.user,
            jenis='Motor',
            merk='Honda',
            tipe='Beat',
            tahun=2024,
            nomor_polisi='N1234AB',
            warna='Hitam'
        )

        self.assertEqual(kendaraan.merk, 'Honda')


class BookingServisModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser2',
            password='12345678'
        )

        self.kendaraan = Kendaraan.objects.create(
            pemilik=self.user,
            jenis='Motor',
            merk='Yamaha',
            tipe='NMAX',
            tahun=2023,
            nomor_polisi='N5678CD',
            warna='Putih'
        )

    def test_create_booking(self):
        booking = BookingServis.objects.create(
            kendaraan=self.kendaraan,
            tanggal_booking='2026-07-30',
            jam_booking='09:00',
            keluhan='Mesin berisik'
        )

        self.assertEqual(booking.status, 'menunggu')