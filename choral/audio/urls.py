from django.urls import path

from . import loader1
from . import views

app_name = 'audio'

urlpatterns = [
    path('ok/', views.ok, name='ok'),
    path('loader1/<str:file_name>', loader1.LoaderView.as_view(), name='loader1'),
    path('', views.index, name='index'),
    path('artist/', views.ArtistListView.as_view(), name='artist')
]
