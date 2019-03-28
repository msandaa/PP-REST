from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from API.models import Produktpass, Massnahmen
from API.serializers import ProduktpassSerializers, MassnahmenSerializers, UserSerializer
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.reverse import reverse
from API.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets



# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('api:users', request=request, format=format),
        'produktpass': reverse('api:produktpass', request=request, format=format),
        'massnahmen': reverse('api:massnahmen', request=request, format=format)
    })

class ProduktpassList(generics.ListCreateAPIView):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Produktpass.objects.all()
    serializer_class = ProduktpassSerializers


class ProduktpassDetail(generics.RetrieveUpdateDestroyAPIView):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Produktpass.objects.all()
    serializer_class = ProduktpassSerializers

class MassnahmenList(generics.ListCreateAPIView):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Massnahmen.objects.all()
    serializer_class = MassnahmenSerializers

class MassnahmenDetail(generics.RetrieveUpdateDestroyAPIView):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Massnahmen.objects.all()
    serializer_class = MassnahmenSerializers

class UserList(generics.ListAPIView):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
