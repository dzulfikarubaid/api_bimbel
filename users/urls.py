from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index),
    path('add_siswa/', views.addSiswa, name='add_siswa'),
    path('add_ortu/', views.addOrtu, name='add_ortu'),
    path('add_mapel/', views.addMapel, name='add_mapel'),
    path('add_pengajar/', views.addPengajar, name='add_pengajar'),
    path('add_paket/', views.addPaket, name='add_paket'),
    path('add_pendaftaran/', views.addPendaftaran, name='add_pendaftaran'),
    path('view_siswa/',views.viewSiswa, name='view_siswa'),
    path('view_ortu/',views.viewOrtu, name='view_ortu'),
    path('view_mapel/',views.viewMapel, name='view_mapel'),
    path('view_pengajar/',views.viewPengajar, name='view_pengajar'),
    path('view_paket/',views.viewPaket, name='view_paket'),
    path('view_pendaftaran/',views.viewPendaftaran, name='view_pendaftaran'),
    path('update_siswa/<int:id_siswa>/',views.updateSiswa, name='update_siswa'),
    path('update_ortu/<int:id_ortu>/',views.updateOrtu, name='update_ortu'),
    path('update_mapel/<int:id_mapel>/',views.updateMapel, name='update_mapel'),
    path('update_pengajar/<int:id_pengajar>/',views.updatePengajar, name='update_pengajar'),
    path('update_paket/<int:id_paket>/',views.updatePaket, name='update_paket'),
    path('update_pendaftaran/<int:nomor_pendaftaran>/',views.updatePendaftaran, name='update_pendaftaran'),
    path('delete_siswa/<int:id_siswa>/',views.deleteSiswa, name='delete_siswa'),
    path('delete_ortu/<int:id_ortu>/',views.deleteOrtu, name='delete_ortu'),
    path('delete_mapel/<int:id_mapel>/',views.deleteMapel, name='delete_mapel'),
    path('delete_pengajar/<int:id_pengajar>/',views.deletePengajar, name='delete_pengajar'),
    path('delete_paket/<int:id_paket>/',views.deletePaket, name='delete_paket'),
    path('delete_pendaftaran/<int:nomor_pendaftaran>/',views.deletePendaftaran, name='delete_pendaftaran'),
]