from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from API.models import Agrarprodukt,Anbau,Anbaumassnahmen
from API.serializers import AgrarproduktSerializers, UserSerializer,AnbauSerializers,AnbaumassnahmenSerializers
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.reverse import reverse
from API.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('api:users', request=request, format=format),
        'agrarprodukt': reverse('api:agrarprodukt', request=request, format=format),
        'anbau': reverse('api:anbau', request=request, format=format),
        'anbaumassnahmen': reverse('api:anbaumassnahmen', request=request,format=format)
    })

class AgrarproduktList(generics.ListCreateAPIView):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Agrarprodukt.objects.all()
    serializer_class = AgrarproduktSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('agrarprodukt',)


class AgrarproduktDetail(generics.RetrieveUpdateDestroyAPIView):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Agrarprodukt.objects.all()
    serializer_class = AgrarproduktSerializers


class AnbauViewSet(viewsets.ModelViewSet):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Anbau.objects.all()
    serializer_class = AnbauSerializers
'''
class AnbauList(generics.ListCreateAPIView):
    queryset = Anbau.objects.all()
    serializer_class = AnbauSerializers

class AnbauDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anbau.objects.all()
    serializer_class = AnbauSerializers'''


class AnbaumassnahmenViewSet(viewsets.ModelViewSet):

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Anbaumassnahmen.objects.all()
    serializer_class = AnbaumassnahmenSerializers


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
