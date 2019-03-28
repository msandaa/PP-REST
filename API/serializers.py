from rest_framework import serializers
from .models import Produktpass,Massnahmen
from django.contrib.auth.models import User





class MassnahmenSerializers(serializers.ModelSerializer):

    #url = serializers.HyperlinkedIdentityField(view_name='api:massnahmen-detail', read_only=True)

    class Meta:
        model = Massnahmen
        fields = ('id','datum','bearbeitung', 'produktpass', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='api:users-detail', read_only=True)
    massnahmen = serializers.HyperlinkedRelatedField(many=True, view_name='api:massnahmen-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id','url', 'username', 'massnahmen')

class ProduktpassSerializers(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='api:produktpass-detail', read_only=True)
    massnahmen = serializers.HyperlinkedRelatedField(many=True, view_name='api:massnahmen-detail', read_only=True)

    class Meta:
        model = Produktpass
        fields = ('id','url','agrarprodukt','los_chargen','longitude','latitude','nutzflächennr', 'massnahmen')
