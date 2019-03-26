from rest_framework import serializers
from .models import Produktpass,Massnahmen
from django.contrib.auth.models import User





class MassnahmenSerializers(serializers.ModelSerializer):


    class Meta:
        model = Massnahmen
        fields = ('id','datum','bearbeitung', 'produktpass', 'owner')


class UserSerializer(serializers.ModelSerializer):
    massnahmen = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'massnahmen')

class ProduktpassSerializers(serializers.ModelSerializer):
    massnahmen = serializers.StringRelatedField(many=True)

    class Meta:
        model = Produktpass
        fields = ('id','agrarprodukt','los_chargen','longitude','latitude','nutzflächennr', 'massnahmen')
