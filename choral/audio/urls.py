from django.urls import path

from . import views

app_name = 'audio'

urlpatterns = [
    path('ok/', views.ok, name='ok'),
    path('xml/', views.ok, name='xml'),
]
