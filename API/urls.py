
from django.urls import path
from . import views
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [

    path('', views.api_root),

    path('produktpass/', views.ProduktpassList.as_view(), name='produktpass'),
    path('produktpass/<str:name>/', views.ProduktpassDetail.as_view(), name='produktpass_show'),

    path('massnahmen/', views.MassnahmenList.as_view(), name='massnahmen'),
    path('massnahmen/<int:pk>', views.MassnahmenDetail.as_view(), name='massnahmen'),

    path('users/', views.UserList.as_view(), name = 'users'),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    ]
