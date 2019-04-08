
from django.urls import path
from . import views
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token


from API.views import  UserViewSet, api_root, AnbaumassnahmenViewSet, AnbauViewSet,ProduktViewSet,ProduktmassnahmenViewSet
from rest_framework import renderers

anbau_list = AnbauViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
anbau_detail = AnbauViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

anbaumassnahmen_list = AnbaumassnahmenViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
anbaumassnahmen_detail = AnbaumassnahmenViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

produkt_list = ProduktViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
produkt_detail = ProduktViewSet.as_view({
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
    'put': 'update',
    'patch': 'partial_update',
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

    path('agrarprodukt/', views.AgrarproduktList.as_view(), name='agrarprodukt'),
    path('agrarprodukt/<int:pk>/', views.AgrarproduktDetail.as_view(), name='agrarprodukt-detail'),

    path('anbau/', anbau_list, name='anbau'),
    path('anbau/<int:pk>', anbau_detail, name='anbau-detail'),

    path('anbaumassnahmen/', anbaumassnahmen_list, name='anbaumassnahmen'),
    path('anbaumassnahmen/<int:pk>', anbaumassnahmen_detail, name='anbaumassnahmen-detail'),

    path('produkt/', produkt_list, name='produkt'),
    path('produkt/<int:pk>', produkt_detail, name='produkt-detail'),

    path('produktmassnahmen/', produktmassnahmen_list, name='produktmassnahmen'),
    path('produktmassnahmen/<int:pk>', produktmassnahmen_detail, name='produktmassnahmen-detail'),

    path('users/', user_list, name = 'users'),
    path('users/<int:pk>/', user_detail, name = 'users-detail'),

    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    ]
