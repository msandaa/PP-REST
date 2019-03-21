from rest_framework import serializers
from .models import Produktpass,Massnahmen

#class ProduktpassSerializers(serializers.Serializer):

#    id = serializers.IntegerField(read_only=True)
#    agrarprodukt = serializers.CharField(max_length=50)
#    los_chargen = serializers.CharField(max_length=50)
#    longitude = serializers.FloatField()
#    latitude = serializers.FloatField()
#    nutzflächennr = serializers.CharField(max_length=50)

#class MassnahmenSerializers(serializers.Serializer):

#    id = serializers.IntegerField(read_only=True)
#    datum = serializers.DateTimeField(auto_now=True)
#    bearbeitung = serializers.CharField(max_length=50)
#    #produktpass = models.ForeignKey(Produktpass, related_name='choices', on_delete=models.CASCADE)

class ProduktpassSerializers(serializers.ModelSerializer):

    class Meta:
        model = Produktpass
        fields = ('agrarprodukt','los_chargen','longitude','latitude','nutzflächennr')

class MassnahmenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Massnahmen
        fields = ('datum','bearbeitung')
