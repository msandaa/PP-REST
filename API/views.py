from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from API.models import Produktpass, Massnahmen
from API.serializers import ProduktpassSerializers, MassnahmenSerializers

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def produktpass(request):

    if request.method == 'GET':
        seri = ProduktpassSerializers(Produktpass.objects.all(), many=True)
        return Response(seri.data)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProduktpassSerializers(data=data)
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
        data = JSONParser().parse(request)
        serializer = ProduktpassSerializers(produktpass,data=data)
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
