from rest_framework import serializers
from .models import Agrarprodukte,Nutzflaechen,Nutzflaechenmassnahmen,Produkt,Produktmassnahmen
from django.contrib.auth.models import User


class ProduktSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Produkt
        fields = ('id','url','produktname', 'produktbeschreibung','agrarprodukt','produktmassnahmen' , 'produkte')
        extra_kwargs = {
            'url': {'view_name': 'api:produkt-detail'},
            'produkte': {'view_name': 'api:produkt-detail'},
            'agrarprodukt' : {'view_name' : 'api:agrarprodukte-detail'},
            'produktmassnahmen' : {'view_name' : 'api:produktmassnahmen-detail'}
        }

class ProduktmassnahmenSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Produktmassnahmen
        fields = ('id','url','name', 'beschreibung','produkt')
        extra_kwargs = {
            'url': {'view_name': 'api:produktmassnahmen-detail'},
            'produkt': {'view_name': 'api:produkt-detail'}
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id','url', 'username','nutzflaeche','nutzflaechenmassnahmen')
        extra_kwargs = {
            'url': { 'view_name' :'api:users-detail'},
            'nutzflaeche': {'view_name' : 'api:nutzflaechen-detail'},
            'nutzflaechenmassnahmen': {'view_name' : 'api:nutzflaechenmassnahmen-detail'}
        }

class AgrarprodukteSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Agrarprodukte
        fields = ('id','url','agrarprodukt','los_chargennummer','nutzflaeche','produkt')
        extra_kwargs = {
            'url': { 'view_name' :'api:agrarprodukte-detail'},
            'nutzflaeche': {'view_name' : 'api:nutzflaechen-detail'},
            'produkt': {'view_name' : 'api:produkt-detail'}
        }

class NutzflaechenSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Nutzflaechen
        fields = ('id','url','nutzflaechennr', 'nutzflaeche','agrarprodukt' ,'verantwortlicher','nutzflaechenmassnahmen')
        extra_kwargs = {
            'url': {'view_name': 'api:nutzflaechen-detail'},
            'agrarprodukt': {'view_name': 'api:agrarprodukte-detail'},
            'nutzflaechenmassnahmen': {'view_name': 'api:nutzflaechenmassnahmen-detail'},
            'verantwortlicher': {'view_name': 'api:users-detail'}
        }


class NutzflaechenmassnahmenSerializers(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='api:nutzflaechenmassnahmen-detail', read_only=True)

    nutzflaechen = serializers.HyperlinkedRelatedField(view_name='api:nutzflaechen-detail', queryset = Nutzflaechen.objects.all())
    verantwortlicher = serializers.HyperlinkedRelatedField(view_name='api:users-detail',queryset = User.objects.all())


    class Meta:
        model = Nutzflaechenmassnahmen
        fields = ('id','url' ,'massnahme','landwirtschftliches_nutzfahrzeug','startuhrzeit_der_bearbeitung','nutzflaechen','verantwortlicher')
        extra_kwargs = {
            'url': { 'view_name' :'api:nutzflaechenmassnahmen-detail'},
            'nutzflaechen': {'view_name' : 'api:nutzflaechen-detail'},
            'verantwortlicher': {'view_name' : 'api:users-detail'}
        }



class AgrarprodukteShowAllSerializer(serializers.ModelSerializer):


    class NutzflaechenShowAllSerializers(serializers.ModelSerializer):

        class NutzflaechenmassnahmenShowAllSerializers(serializers.ModelSerializer):

            class Meta:
                model = Nutzflaechenmassnahmen
                fields = ('id' ,'massnahme','landwirtschftliches_nutzfahrzeug','startuhrzeit_der_bearbeitung','verantwortlicher')

        nutzflaechenmassnahmen = NutzflaechenmassnahmenShowAllSerializers(many=True ,read_only = True)

        class Meta:
            model = Nutzflaechen
            fields = ('id','nutzflaechennr', 'nutzflaeche','verantwortlicher' ,'nutzflaechenmassnahmen')


    nutzflaeche = NutzflaechenShowAllSerializers(read_only = True)

    class Meta:
        model = Agrarprodukte
        fields = ('id','agrarprodukt','los_chargennummer','produkt','nutzflaeche')


class ProduktmassnahmenShowAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produktmassnahmen
        fields = ('id','name', 'beschreibung')


class SubSubSubSubProduktShowAllSerializer(serializers.ModelSerializer):

    #produkte = ProduktShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkt
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')

class SubSubSubProduktShowAllSerializer(serializers.ModelSerializer):

    produkte = SubSubSubSubProduktShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkt
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')

class SubSubProduktShowAllSerializer(serializers.ModelSerializer):

    produkte = SubSubSubProduktShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkt
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')

class SubProduktShowAllSerializer(serializers.ModelSerializer):

    produkte = SubSubProduktShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkt
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')

class ProduktShowAllSerializer(serializers.ModelSerializer):

    produkte = SubProduktShowAllSerializer(many = True , read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkt
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')
