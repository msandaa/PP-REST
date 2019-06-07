from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from API.models import Agrarprodukte,Nutzflaechen,Nutzflaechenmassnahmen,Produkte,Produktmassnahmen
from API.serializers import AgrarprodukteSerializers, UserSerializer,NutzflaechenSerializers,NutzflaechenmassnahmenSerializers,ProdukteSerializers,ProduktmassnahmenSerializers,ProdukteShowAllSerializer,AgrarprodukteShowAllSerializer
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.reverse import reverse
#from API.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('api:users', request=request, format=format),
        'produkte': reverse('api:produkte',request = request,format=format),
        'produktmassnahmen': reverse('api:produktmassnahmen',request = request,format=format),
        'agrarprodukte': reverse('api:agrarprodukte', request=request, format=format),
        'nutzflaechen': reverse('api:nutzflaechen', request=request, format=format),
        'nutzflaechenmassnahmen': reverse('api:nutzflaechenmassnahmen', request=request,format=format)
    })


class AgrarprodukteList(generics.ListCreateAPIView):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #-- wird nicht benötigt, da in setting.py schon als default deklariert ist

    queryset = Agrarprodukte.objects.all()
    serializer_class = AgrarprodukteSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('agrarprodukt',)


class AgrarprodukteDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Agrarprodukte.objects.all()
    serializer_class = AgrarprodukteSerializers

#
#
# OB hier generics. oder veiwsets. als View-Klasse gewählt wird macht hier nur geringen unterschied
# Durch Refraktormßnahmen könnten AgrarproduktList und AgrarproduktDetail zu einem ViewSet zusammengefasst werden
# siehe: https://www.django-rest-framework.org/api-guide/generic-views/
# siehe: https://www.django-rest-framework.org/api-guide/viewsets/
#
#

class NutzflaechenViewSet(viewsets.ModelViewSet):

    queryset = Nutzflaechen.objects.all()
    serializer_class = NutzflaechenSerializers

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('agrarprodukt',)

class ProdukteViewSet(viewsets.ModelViewSet):

    queryset = Produkte.objects.all()
    serializer_class = ProdukteSerializers

class ProduktmassnahmenViewSet(viewsets.ModelViewSet):

    queryset = Produktmassnahmen.objects.all()
    serializer_class = ProduktmassnahmenSerializers

class NutzflaechenmassnahmenViewSet(viewsets.ModelViewSet):

    queryset = Nutzflaechenmassnahmen.objects.all()
    serializer_class = NutzflaechenmassnahmenSerializers

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('nutzflaeche',)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer





@api_view(['GET'])
def ProdukteShowAll(request, pk):

    try:
        produkt = Produkte.objects.get(pk=pk)
    except Produkte.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProdukteShowAllSerializer(produkt, context={'request': request})
        return Response(serializer.data)

@api_view(['GET'])
def AgrarprodukteShowAll(request, pk):

    try:
        agrarprodukt = Agrarprodukte.objects.get(pk=pk)
    except Agrarprodukte.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AgrarprodukteShowAllSerializer(agrarprodukt, context={'request': request})
        return Response(serializer.data)
