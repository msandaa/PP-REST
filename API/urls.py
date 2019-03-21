
from django.urls import path
from . import views

urlpatterns = [
    path('produktpass/', views.produktpass, name='produktpass'),
    path('massnahmen/', views.massnahmen, name='massnahmen'),
    path('produktpass/<str:name>/', views.produktpass_detail, name='produktpass_show'),
]
