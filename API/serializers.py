from rest_framework import serializers
from .models import Agrarprodukt,Anbau,Anbaumassnahmen,Produkt,Produktmassnahmen
from django.contrib.auth.models import User


class ProduktSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Produkt
        fields = ('id','url','produktname', 'produktbeschreibung','agrarprodukt','produktmassnahmen' , 'produkte')
        extra_kwargs = {
            'url': {'view_name': 'api:produkt-detail'},
            'produkte': {'view_name': 'api:produkt-detail'},
            'agrarprodukt' : {'view_name' : 'api:agrarprodukt-detail'},
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
        fields = ('id','url', 'username','anbau','anbaumassnahmen')
        extra_kwargs = {
            'url': { 'view_name' :'api:users-detail'},
            'anbau': {'view_name' : 'api:anbau-detail'},
            'anbaumassnahmen': {'view_name' : 'api:anbaumassnahmen-detail'}
        }

class AgrarproduktSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Agrarprodukt
        fields = ('id','url','agrarprodukt','los_chargennummer','anbau','produkt')
        extra_kwargs = {
            'url': { 'view_name' :'api:agrarprodukt-detail'},
            'anbau': {'view_name' : 'api:anbau-detail'},
            'produkt': {'view_name' : 'api:produkt-detail'}
        }

class AnbauSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Anbau
        fields = ('id','url','nutzflaechennr', 'nutzflaeche','agrarprodukt' ,'verantwortlicher','anbaumassnahmen')
        extra_kwargs = {
            'url': {'view_name': 'api:anbau-detail'},
            'agrarprodukt': {'view_name': 'api:agrarprodukt-detail'},
            'anbaumassnahmen': {'view_name': 'api:anbaumassnahmen-detail'},
            'verantwortlicher': {'view_name': 'api:users-detail'}
        }


class AnbaumassnahmenSerializers(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='api:anbaumassnahmen-detail', read_only=True)

    anbau = serializers.HyperlinkedRelatedField(view_name='api:anbau-detail', queryset = Anbau.objects.all())
    verantwortlicher = serializers.HyperlinkedRelatedField(view_name='api:users-detail',queryset = User.objects.all())


    class Meta:
        model = Anbaumassnahmen
        fields = ('id','url' ,'massnahme','landwirtschftliches_nutzfahrzeug','startuhrzeit_der_bearbeitung','anbau','verantwortlicher')
        extra_kwargs = {
            'url': { 'view_name' :'api:anbaumassnahmen-detail'},
            'anbau': {'view_name' : 'api:anbau-detail'},
            'verantwortlicher': {'view_name' : 'api:users-detail'}
        }



class AgrarproduktShowAllSerializer(serializers.ModelSerializer):


    class AnbauShowAllSerializers(serializers.ModelSerializer):

        class AnbaumassnahmenShowAllSerializers(serializers.ModelSerializer):

            class Meta:
                model = Anbaumassnahmen
                fields = ('id' ,'massnahme','landwirtschftliches_nutzfahrzeug','startuhrzeit_der_bearbeitung','verantwortlicher')

        anbaumassnahmen = AnbaumassnahmenShowAllSerializers(many=True ,read_only = True)

        class Meta:
            model = Anbau
            fields = ('id','nutzflaechennr', 'nutzflaeche','verantwortlicher' ,'anbaumassnahmen')


    anbau = AnbauShowAllSerializers(read_only = True)

    class Meta:
        model = Agrarprodukt
        fields = ('id','agrarprodukt','los_chargennummer','produkt','anbau')


class ProduktmassnahmenShowAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produktmassnahmen
        fields = ('id','name', 'beschreibung')


class SubSubSubSubProduktShowAllSerializer(serializers.ModelSerializer):

    #produkte = ProduktShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarproduktShowAllSerializer(read_only = True)

    class Meta:
        model = Produkt
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')

class SubSubSubProduktShowAllSerializer(serializers.ModelSerializer):

    produkte = SubSubSubSubProduktShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarproduktShowAllSerializer(read_only = True)

    class Meta:
        model = Produkt
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')

class SubSubProduktShowAllSerializer(serializers.ModelSerializer):

    produkte = SubSubSubProduktShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarproduktShowAllSerializer(read_only = True)

    class Meta:
        model = Produkt
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')

class SubProduktShowAllSerializer(serializers.ModelSerializer):

    produkte = SubSubProduktShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarproduktShowAllSerializer(read_only = True)

    class Meta:
        model = Produkt
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')

class ProduktShowAllSerializer(serializers.ModelSerializer):

    produkte = SubProduktShowAllSerializer(many = True , read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    agrarprodukt = AgrarproduktShowAllSerializer(read_only = True)

    class Meta:
        model = Produkt
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','produkte','agrarprodukt')
