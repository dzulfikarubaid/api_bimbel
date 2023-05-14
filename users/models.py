from django.db import models

# Create your models here.


class modelOrtu(models.Model):
    id_ortu = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=250)
    jenis_kelamin = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    nomor_telepon = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id_ortu) + " | " + self.nama


class modelPengajar(models.Model):
    id_pengajar = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    def __str__(self):
        return str(self.id_pengajar) + " | " +self.nama
        
class modelPaket(models.Model):
    id_paket = models.AutoField(primary_key=True)
    nama_paket = models.CharField(max_length=100)
    def __str__(self):
        return str(self.id_paket) + " | " +self.nama_paket

class modelMapel(models.Model):
    id_mapel = models.AutoField(primary_key=True)
    nama_mapel = models.CharField(max_length=100)
    id_pengajar = models.ForeignKey(modelPengajar, on_delete=models.CASCADE)
    id_paket = models.ForeignKey(modelPaket, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_mapel) + " | " +self.nama_mapel

class modelSiswa(models.Model):
    id_siswa = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=50)
    usia = models.IntegerField()
    id_ortu = models.ForeignKey(modelOrtu, on_delete=models.CASCADE)
    id_paket = models.ForeignKey(modelPaket, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_siswa) + " | " +self.nama

class modelPendaftaran(models.Model):
    no_pendaftaran = models.AutoField(primary_key=True)
    tanggal_pendaftaran = models.DateField(auto_now_add=True)
    id_ortu = models.ForeignKey(modelOrtu, on_delete=models.CASCADE)
    id_siswa = models.ForeignKey(modelSiswa, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.no_pendaftaran) + " | " + str(self.tanggal_pendaftaran)
