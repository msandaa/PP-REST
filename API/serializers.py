from rest_framework import serializers
from .models import Agrarprodukte,Nutzflaechen,Nutzflaechenmassnahmen,Produkte,Produktmassnahmen
from django.contrib.auth.models import User


class ProdukteSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Produkte
        fields = ('id','url','produktname', 'produktbeschreibung','agrarprodukt','produktmassnahmen' , 'produkte')
        extra_kwargs = {
            'url': {'view_name': 'api:produkte-detail'},
            'produkte': {'view_name': 'api:produkte-detail'},
            'agrarprodukt' : {'view_name' : 'api:agrarprodukte-detail'},
            'produktmassnahmen' : {'view_name' : 'api:produktmassnahmen-detail'}
        }

class ProduktmassnahmenSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Produktmassnahmen
        fields = ('id','url','name', 'beschreibung','produkt')
        extra_kwargs = {
            'url': {'view_name': 'api:produktmassnahmen-detail'},
            'produkt': {'view_name': 'api:produkte-detail'}
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
            'produkt': {'view_name' : 'api:produkte-detail'}
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


class SubSubSubSubProdukteShowAllSerializer(serializers.ModelSerializer):

    #produkte = ProduktShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkte
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')

class SubSubSubProdukteShowAllSerializer(serializers.ModelSerializer):

    produkte = SubSubSubSubProdukteShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkte
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')

class SubSubProdukteShowAllSerializer(serializers.ModelSerializer):

    produkte = SubSubSubProdukteShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkte
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')

class SubProdukteShowAllSerializer(serializers.ModelSerializer):

    produkte = SubSubProdukteShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkte
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')

class ProdukteShowAllSerializer(serializers.ModelSerializer):

    produkte = SubProdukteShowAllSerializer(many = True , read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkte
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')
