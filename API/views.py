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



# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users', request=request, format=format),
        'produktpass': reverse('produktpass', request=request, format=format),
        'massnahmen': reverse('massnahmen', request=request, format=format)
    })

class ProduktpassList(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)

    def get(self, request, format=None):
        produktpass = Produktpass.objects.all()
        serializer = ProduktpassSerializers(produktpass, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProduktpassSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProduktpassDetail(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, name):
        try:
            return Produktpass.objects.get(agrarprodukt__exact = name)
        except Produktpass.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        produktpass = self.get_object(name)
        serializer = ProduktpassSerializers(produktpass)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        produktpass = self.get_object(name)
        serializer = ProduktpassSerializers(produktpass, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        produktpass = self.get_object(name)
        produktpass.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class MassnahmenList(generics.ListAPIView):

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


"""
@csrf_exempt
@api_view(['GET', 'POST'])
def produktpass(request):

    if request.method == 'GET':
        seri = ProduktpassSerializers(Produktpass.objects.all(), many=True)
        return Response(seri.data)


    elif request.method == 'POST':
        serializer = ProduktpassSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT','DELETE'])
def produktpass_detail(request,name):

    try:
        produktpass = Produktpass.objects.get(agrarprodukt__exact = name)
    except produktpass.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        seri = ProduktpassSerializers(produktpass)
        return Response(seri.data)

    elif request.method == 'PUT':
        serializer = ProduktpassSerializers(produktpass,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        produktpass.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def massnahmen(request):

    if request.method == 'GET':

        seri = MassnahmenSerializers(Massnahmen.objects.all(), many=True)

        return Response(seri.data, safe = False)

"""
