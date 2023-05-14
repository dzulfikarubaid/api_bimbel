from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import serializerMapel, serializerSiswa, serializerOrtu, serializerPendaftaran, serializerPengajar, serializerPaket
from .models import modelMapel, modelSiswa, modelOrtu, modelPendaftaran, modelPengajar, modelPaket
# Create your views here.
def index(request):
    return redirect('docs/')
@api_view(['POST'])
def addSiswa(request):
    serializer = serializerSiswa(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({serializer.data})
    return Response(serializer.errors)
@api_view(['POST'])
def addOrtu(request):
    serializer = serializerOrtu(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({serializer.data})
    return Response(serializer.errors)
@api_view(['POST'])
def addMapel(request):
    serializer = serializerMapel(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({serializer.data})
    return Response(serializer.errors)
@api_view(['POST'])
def addPengajar(request):
    serializer = serializerPengajar(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({serializer.data})
    return Response(serializer.errors)
@api_view(['POST'])
def addPaket(request):
    serializer = serializerPaket(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({serializer.data})
    return Response(serializer.errors)
@api_view(['POST'])
def addPendaftaran(request):
    serializer = serializerPendaftaran(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({serializer.data})
    return Response(serializer.errors)

@api_view(['GET'])
def viewSiswa(request):
    Object=modelSiswa.objects.all()
    SerializerObject = serializerSiswa(Object,many=True)
    return Response(SerializerObject.data)
@api_view(['GET'])
def viewOrtu(request):
    Object=modelOrtu.objects.all()
    SerializerObject = serializerOrtu(Object,many=True)
    return Response(SerializerObject.data)
@api_view(['GET'])
def viewMapel(request):
    Object=modelMapel.objects.all()
    SerializerObject = serializerMapel(Object,many=True)
    return Response(SerializerObject.data)
@api_view(['GET'])
def viewPengajar(request):
    Object=modelPengajar.objects.all()
    SerializerObject = serializerPengajar(Object,many=True)
    return Response(SerializerObject.data)
@api_view(['GET'])
def viewPaket(request):
    Object=modelPaket.objects.all()
    SerializerObject = serializerPaket(Object,many=True)
    return Response(SerializerObject.data)
@api_view(['GET'])
def viewPendaftaran(request):
    Object=modelPendaftaran.objects.all()
    SerializerObject = serializerPendaftaran(Object,many=True)
    return Response(SerializerObject.data)
@api_view(['PUT'])
def updateSiswa(request, id):
    try:
        ModelObject = modelSiswa.objects.get(id=id_siswa)
    except:
        status = {'status':'data tidak ditemukan'}
        return Response(status)
    serializer = serializerSiswa(ModelObject, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['PUT'])
def updateOrtu(request, id):
    try:
        ModelObject = modelOrtu.objects.get(id=id_ortu)
    except:
        status = {'status':'data tidak ditemukan'}
        return Response(status)
    serializer = serializerOrtu(ModelObject, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['PUT'])
def updateMapel(request, id):
    try:
        ModelObject = modelMapel.objects.get(id=id_mapel)
    except :
        status = {'status':'data tidak ditemukan'}
        return Response(status)
    serializer = serializerMapel(ModelObject, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['PUT'])
def updatePengajar(request, id):
    try:
        ModelObject = modelPengajar.objects.get(id=id_pengajar)
    except:
        status = {'status':'data tidak ditemukan'}
        return Response(status)
    serializer = serializerPengajar(ModelObject, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['PUT'])
def updatePaket(request, id):
    try:
        ModelObject = modelPaket.objects.get(id=id_paket)
    except:
        status = {'status':'data tidak ditemukan'}
        return Response(status)
    serializer = serializerPaket(ModelObject, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['PUT'])
def updatePendaftaran(request, id):
    try:
        ModelObject = modelPendaftaran.objects.get(id=nomor_pendaftaran)
    except:
        status = {'status':'data tidak ditemukan'}
        return Response(status)
    serializer = serializerPendaftaran(ModelObject, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['DELETE'])
def deleteSiswa(request, id):
    try:
        ModelObject = modelSiswa.objects.get(id=id_siswa)
    except:
        status = {'status':'data tidak ditemukan'}
        return Response(status)
    ModelObject.delete()
    return Response({
        'status':'data telah dihapus'
    })
@api_view(['DELETE'])
def deleteOrtu(request, id):
    try:
        ModelObject = modelOrtu.objects.get(id=id_ortu)
    except:
        status = {'status':'data tidak ditemukan'}
        return Response(status)
    ModelObject.delete()
    return Response({
        'status':'data telah dihapus'
    })
@api_view(['DELETE'])
def deletePaket(request, id):
    try:
        ModelObject = modelPaket.objects.get(id=id_paket)
    except:
        status = {'status':'data tidak ditemukan'}
        return Response(status)
    ModelObject.delete()
    return Response({
        'status':'data telah dihapus'
    })
@api_view(['DELETE'])
def deletePendaftaran(request, id):
    try:
        ModelObject = modelPendaftaran.objects.get(id=nomor_pendaftaran)
    except:
        status = {'status':'data tidak ditemukan'}
        return Response(status)
    ModelObject.delete()
    return Response({
        'status':'data telah dihapus'
    })
@api_view(['DELETE'])
def deleteMapel(request, id):
    try:
        ModelObject = modelMapel.objects.get(id=id_mapel)
    except:
        status = {'status':'data tidak ditemukan'}
        return Response(status)
    ModelObject.delete()
    return Response({
        'status':'data telah dihapus'
    })
@api_view(['DELETE'])
def deletePengajar(request, id):
    try:
        ModelObject = modelPengajar.objects.get(id=id_pengajar)
    except:
        status = {'status':'data tidak ditemukan'}
        return Response(status)
    ModelObject.delete()
    return Response({
        'status':'data telah dihapus'
    })