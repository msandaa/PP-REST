
from django.urls import path
from . import views
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token


from API.views import  UserViewSet, api_root, NutzflaechenmassnahmenViewSet, NutzflaechenViewSet,ProdukteViewSet,ProduktmassnahmenViewSet,AgrarprodukteViewSet
from rest_framework import renderers

agrarprodukte_list = AgrarprodukteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
agrarprodukte_detail = AgrarprodukteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

nutzflaechen_list = NutzflaechenViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
nutzflaechen_detail = NutzflaechenViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

nutzflaechenmassnahmen_list = NutzflaechenmassnahmenViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
nutzflaechenmassnahmen_detail = NutzflaechenmassnahmenViewSet.as_view({
    'get': 'retrieve',
#    'put': 'update',                             # Nutzflaechenmassnahmen und Produktmassnahmen
#    'patch': 'partial_update',                   # dürfen nicht geupdatet werden
    'delete': 'destroy'
})

produkte_list = ProdukteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
produkte_detail = ProdukteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

produktmassnahmen_list = ProduktmassnahmenViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
produktmassnahmen_detail = ProduktmassnahmenViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [

    path('', views.api_root),

    path('agrarprodukte/', agrarprodukte_list, name='agrarprodukte'),
    path('agrarprodukte/<int:pk>/', agrarprodukte_detail, name='agrarprodukte-detail'),

    path('nutzflaechen/', nutzflaechen_list, name='nutzflaechen'),
    path('nutzflaechen/<int:pk>', nutzflaechen_detail, name='nutzflaechen-detail'),

    path('nutzflaechenmassnahmen/', nutzflaechenmassnahmen_list, name='nutzflaechenmassnahmen'),
    path('nutzflaechenmassnahmen/<int:pk>', nutzflaechenmassnahmen_detail, name='nutzflaechenmassnahmen-detail'),

    path('produkte/', produkte_list, name='produkte'),
    path('produkte/<int:pk>', produkte_detail, name='produkte-detail'),

    path('produktmassnahmen/', produktmassnahmen_list, name='produktmassnahmen'),
    path('produktmassnahmen/<int:pk>', produktmassnahmen_detail, name='produktmassnahmen-detail'),

    path('users/', user_list, name = 'users'),
    path('users/<int:pk>/', user_detail, name = 'users-detail'),

    path('produkte/<int:pk>/show-all', views.ProdukteShowAll, name='produkte-showAll'),
    path('agrarprodukte/<int:pk>/show-all', views.AgrarprodukteShowAll, name='agrarprodukte-showAll'),

    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    ]
