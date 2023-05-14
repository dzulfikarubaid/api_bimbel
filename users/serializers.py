from rest_framework import serializers
from .models import modelSiswa, modelOrtu, modelPendaftaran, modelPengajar, modelMapel, modelPaket

class serializerSiswa(serializers.ModelSerializer):
    class Meta:
        model = modelSiswa
        fields = '__all__'

class serializerOrtu(serializers.ModelSerializer):
    class Meta:
        model = modelOrtu
        fields = '__all__'

class serializerPendaftaran(serializers.ModelSerializer):
    class Meta:
        model = modelPendaftaran
        fields = '__all__'

class serializerPengajar(serializers.ModelSerializer):
    class Meta:
        model = modelPengajar
        fields = '__all__'

class serializerMapel(serializers.ModelSerializer):
    class Meta:
        model = modelMapel
        fields = '__all__'

class serializerPaket(serializers.ModelSerializer):
    class Meta:
        model = modelPaket
        fields = '__all__'

