from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from API.models import Agrarprodukte,Nutzflaechen,Nutzflaechenmassnahmen,Produkt,Produktmassnahmen
from API.serializers import AgrarprodukteSerializers, UserSerializer,NutzflaechenSerializers,NutzflaechenmassnahmenSerializers,ProduktSerializers,ProduktmassnahmenSerializers,ProduktShowAllSerializer,AgrarprodukteShowAllSerializer
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.reverse import reverse
from API.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('api:users', request=request, format=format),
        'produkt': reverse('api:produkt',request = request,format=format),
        'produktmassnahmen': reverse('api:produktmassnahmen',request = request,format=format),
        'agrarprodukte': reverse('api:agrarprodukte', request=request, format=format),
        'nutzflaechen': reverse('api:nutzflaechen', request=request, format=format),
        'nutzflaechenmassnahmen': reverse('api:nutzflaechenmassnahmen', request=request,format=format)
    })


class AgrarprodukteList(generics.ListCreateAPIView):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Agrarprodukte.objects.all()
    serializer_class = AgrarprodukteSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('agrarprodukt',)


class AgrarprodukteDetail(generics.RetrieveUpdateDestroyAPIView):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Agrarprodukte.objects.all()
    serializer_class = AgrarprodukteSerializers


class NutzflaechenViewSet(viewsets.ModelViewSet):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Nutzflaechen.objects.all()
    serializer_class = NutzflaechenSerializers

class ProduktViewSet(viewsets.ModelViewSet):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializers

class ProduktmassnahmenViewSet(viewsets.ModelViewSet):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Produktmassnahmen.objects.all()
    serializer_class = ProduktmassnahmenSerializers



class NutzflaechenmassnahmenViewSet(viewsets.ModelViewSet):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Nutzflaechenmassnahmen.objects.all()
    serializer_class = NutzflaechenmassnahmenSerializers


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def ProduktShowAll(request, pk):

    try:
        produkt = Produkt.objects.get(pk=pk)
    except Produkt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProduktShowAllSerializer(produkt, context={'request': request})
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
