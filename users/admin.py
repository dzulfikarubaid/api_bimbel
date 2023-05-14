from django.contrib import admin
from .models import modelSiswa, modelOrtu, modelPendaftaran, modelPengajar, modelMapel, modelPaket
# Register your models here.
myModels = [modelSiswa, modelOrtu, modelPendaftaran, modelPengajar, modelMapel, modelPaket]  # iterable list
admin.site.register(myModels)