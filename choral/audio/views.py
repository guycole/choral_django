from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.views import generic

from .models import Album
from .models import Artist
from .models import Track

def ok(request):
    return HttpResponse('audio ok')

def index(request):
    album_population = Album.objects.all().count()
    artist_population = Artist.objects.all().count()
    track_population = Track.objects.all().count()

    context = {
        'album_population': album_population,
        'artist_population': artist_population,
        'track_population': track_population,
    }

    return render(request, 'audio/index.html', context=context)


class IndexView(generic.ListView):
    template_name = 'audio/artist_index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Artist.objects.order_by('-last_name')[:5]

class ArtistListView(generic.ListView):
    model = Artist

#path('artist/', views.ArtistListView.as_view(), name='artist')