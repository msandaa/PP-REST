from rest_framework import serializers
from .models import Agrarprodukt,Anbau,Anbaumassnahmen
from django.contrib.auth.models import User




class UserSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='api:users-detail', read_only=True)

    anbau = serializers.HyperlinkedRelatedField(many=True,view_name='api:anbau-detail', queryset = Anbau.objects.all())
    anbaumassnahmen = serializers.HyperlinkedRelatedField(many=True, view_name='api:anbaumassnahmen-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id','url', 'username','anbau','anbaumassnahmen')

class AgrarproduktSerializers(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='api:agrarprodukt-detail', read_only=True)

    anbau = serializers.HyperlinkedIdentityField(many=True,view_name='api:anbau-detail', read_only=True)

    class Meta:
        model = Agrarprodukt
        fields = ('id','url','agrarprodukt','los_chargennummer','anbau')

class AnbauSerializers(serializers.HyperlinkedModelSerializer):

    #url = serializers.HyperlinkedIdentityField(view_name='api:anbau-detail', read_only=True)

    #anbaumassnahmen = serializers.HyperlinkedRelatedField(many=True, view_name='api:anbaumassnahmen-detail', read_only=True)
    #agrarprodukt = serializers.HyperlinkedRelatedField(view_name='api:agrarprodukt-detail',queryset = Agrarprodukt.objects.all())
    #verantwortlicher = serializers.HyperlinkedRelatedField(view_name='api:users-detail',queryset = User.objects.all())

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
