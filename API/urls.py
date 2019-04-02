
from django.urls import path
from . import views
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token


from API.views import MassnahmenViewSet, UserViewSet, api_root
from rest_framework import renderers

massnahmen_list = MassnahmenViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
massnahmen_detail = MassnahmenViewSet.as_view({
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

    path('produktpass/', views.ProduktpassList.as_view(), name='produktpass'),
    path('produktpass/<int:pk>/', views.ProduktpassDetail.as_view(), name='produktpass-detail'),

    path('massnahmen/', massnahmen_list, name='massnahmen'),
    path('massnahmen/<int:pk>', massnahmen_detail, name='massnahmen-detail'),

    path('users/', user_list, name = 'users'),
    path('users/<int:pk>/', user_detail, name = 'users-detail'),

    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    ]
