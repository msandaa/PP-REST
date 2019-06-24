from rest_framework import serializers
from .models import Agrarprodukte,Nutzflaechen,Nutzflaechenmassnahmen,Produkte,Produktmassnahmen
from django.contrib.auth.models import User

#Mehr Informationen
#
#über HyperLinkedmodelserializer:
#https://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer
#
#über Hyperlinked Views in Meta-Klasse mit extra_kwargs_:
#https://www.django-rest-framework.org/api-guide/serializers/#how-hyperlinked-views-are-determined
#
#über read_only_fields in Meta-Klasse:
#https://www.django-rest-framework.org/api-guide/serializers/#specifying-read-only-fields
#
#siehe Kommentar in NutzflaechenmassnahmenSerializers um eine andere Art und Weise
#Verknüpfungen über Hyperlinks zu erstellen kennenzulernen
#
#
#


class ProdukteSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Produkte
        fields = ('id','url','produktname', 'produktbeschreibung','produktmassnahmen','hergestellt_aus_agrarprodukt', 'besteht_aus_produkte')
        extra_kwargs = {
            'url': {'view_name': 'api:produkte-detail'},
            'produktmassnahmen' : {'view_name' : 'api:produktmassnahmen-detail'},
            'hergestellt_aus_agrarprodukt' : {'view_name' : 'api:agrarprodukte-detail'},
            'besteht_aus_produkte': {'view_name': 'api:produkte-detail'},
            }
        read_only_fields = ('produktmassnahmen',)


class ProduktmassnahmenSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Produktmassnahmen
        fields = ('id','url','massnahme', 'beschreibung','produkt')
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
        fields = ('id','url','agrarprodukt','los_chargennummer','produktionsart','produzent_name','produzent_straße','produzent_ort','angebaut_auf_nutzflaeche','wird_verwendet_in_produkte')
        extra_kwargs = {
            'url': { 'view_name' :'api:agrarprodukte-detail'},
            'angebaut_auf_nutzflaeche': {'view_name' : 'api:nutzflaechen-detail'},
            'wird_verwendet_in_produkte': {'view_name' : 'api:produkte-detail'}
        }
        read_only_fields = ('wird_verwendet_in_produkte',)

        # wird_verwendet_in_produkte ist read_only weil die Verknüpfen Produkt-Agraprodukt über das Produkt hergestellt wird

class NutzflaechenSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Nutzflaechen
        fields = ('id','url','nutzflaechennummer','boxnummer','kreisnummer','kreis','bundeslandnummer','bundesland', 'nutzflaeche_in_ha','agrarprodukt' ,'verantwortlicher','nutzflaechenmassnahmen')
        extra_kwargs = {
            'url': {'view_name': 'api:nutzflaechen-detail'},
            'agrarprodukt': {'view_name': 'api:agrarprodukte-detail'},
            'nutzflaechenmassnahmen': {'view_name': 'api:nutzflaechenmassnahmen-detail'},
            'verantwortlicher': {'view_name': 'api:users-detail'}
        }
        read_only_fields = ('nutzflaechenmassnahmen','agrarprodukt',)

        #nutzflaechenmassnahmen sind read_only da sie nicht mehr verändert werden dürfen
        #agrarproduk ist read_only weil die Verknüpfen zum agrarprodukt immer über das Agrarprodukt selbst hergestellt wird


class NutzflaechenmassnahmenSerializers(serializers.HyperlinkedModelSerializer):


    #Diesen Code, müsste man benutzen, würde man die Felder nicht in der Meta-Klasse deklarieren
    #
    #url = serializers.HyperlinkedIdentityField(view_name='api:nutzflaechenmassnahmen-detail', read_only=True)
    #nutzflaeche = serializers.HyperlinkedRelatedField(view_name='api:nutzflaechen-detail', queryset = Nutzflaechen.objects.all())
    #verantwortlicher = serializers.HyperlinkedRelatedField(view_name='api:users-detail',queryset = User.objects.all())
    #
    #siehe auch: https://www.django-rest-framework.org/api-guide/relations/#serializer-relations

    class Meta:
        model = Nutzflaechenmassnahmen
        fields = ('id','url' ,'massnahme','landwirtschftliches_nutzfahrzeug','datum','startuhrzeit_der_bearbeitung','enduhrzeit_der_bearbeitung','zeitdifferenz','bearbeitungszeit','unterbrechungszeit','zurückgelegte_strecke_in_km','durchschnittliche_fahrgeschwindigkeit_in_kmh','bearbeitungsbreite_in_m','bearbeitet_nutzfläche_in_ha','flächenleistung_in_hah','ausgeführt_auf_nutzflaeche','verantwortlicher')
        extra_kwargs = {
            'url': { 'view_name' :'api:nutzflaechenmassnahmen-detail'},
            'ausgeführt_auf_nutzflaeche': {'view_name' : 'api:nutzflaechen-detail'},
            'verantwortlicher': {'view_name' : 'api:users-detail'}
        }






class AgrarprodukteShowAllSerializer(serializers.ModelSerializer):


    class NutzflaechenShowAllSerializers(serializers.ModelSerializer):

        class NutzflaechenmassnahmenShowAllSerializers(serializers.ModelSerializer):

            class Meta:
                model = Nutzflaechenmassnahmen
                fields = ('id','massnahme','landwirtschftliches_nutzfahrzeug','datum','startuhrzeit_der_bearbeitung','enduhrzeit_der_bearbeitung','zeitdifferenz','bearbeitungszeit','unterbrechungszeit','zurückgelegte_strecke_in_km','durchschnittliche_fahrgeschwindigkeit_in_kmh','bearbeitungsbreite_in_m','bearbeitet_nutzfläche_in_ha','flächenleistung_in_hah','ausgeführt_auf_nutzflaeche','verantwortlicher')

        nutzflaechenmassnahmen = NutzflaechenmassnahmenShowAllSerializers(many=True ,read_only = True)

        class Meta:
            model = Nutzflaechen
            fields = ('id','nutzflaechennummer','boxnummer','kreisnummer','kreis','bundeslandnummer','bundesland', 'nutzflaeche_in_ha','agrarprodukt' ,'verantwortlicher','nutzflaechenmassnahmen')


    angebaut_auf_nutzflaeche = NutzflaechenShowAllSerializers(read_only = True)

    class Meta:
        model = Agrarprodukte
        fields = ('id','agrarprodukt','los_chargennummer','wird_verwendet_in_produkte','angebaut_auf_nutzflaeche')


class ProduktmassnahmenShowAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produktmassnahmen
        fields = ('id','massnahme', 'beschreibung')





class SubSubSubSubProdukteShowAllSerializer(serializers.ModelSerializer):

    #produkte = ProduktShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    hergestellt_aus_agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkte
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','besteht_aus_produkte','hergestellt_aus_agrarprodukt')

class SubSubSubProdukteShowAllSerializer(serializers.ModelSerializer):

    besteht_aus_produkte = SubSubSubSubProdukteShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    hergestellt_aus_agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkte
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','besteht_aus_produkte','hergestellt_aus_agrarprodukt')

class SubSubProdukteShowAllSerializer(serializers.ModelSerializer):

    besteht_aus_produkte = SubSubSubProdukteShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    hergestellt_aus_agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkte
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','besteht_aus_produkte','hergestellt_aus_agrarprodukt')

class SubProdukteShowAllSerializer(serializers.ModelSerializer):

    besteht_aus_produkte = SubSubProdukteShowAllSerializer(many = True,read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    hergestellt_aus_agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkte
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','besteht_aus_produkte','hergestellt_aus_agrarprodukt')

class ProdukteShowAllSerializer(serializers.ModelSerializer):

    besteht_aus_produkte = SubProdukteShowAllSerializer(many = True , read_only = True)
    produktmassnahmen = ProduktmassnahmenShowAllSerializer(many = True, read_only = True)
    hergestellt_aus_agrarprodukt = AgrarprodukteShowAllSerializer(read_only = True)

    class Meta:
        model = Produkte
        fields = ('id','produktname', 'produktbeschreibung','produktmassnahmen','besteht_aus_produkte','hergestellt_aus_agrarprodukt')
