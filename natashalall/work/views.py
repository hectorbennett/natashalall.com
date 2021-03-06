from django.shortcuts import render
from django.utils import timezone
from .models import Artwork


def index(request):
    artworks = Artwork.objects.filter(live=True)
    context = {'artworks': artworks}
    return render(request, 'work/index.html', context)


def artwork_detail(request, pk):
    artwork = Artwork.objects.get(pk=pk)
    images = artwork.images.all().filter(visible=True)
    videos = artwork.videos.all()
    audio_clips = artwork.audio_clips.all()
    exhibitions = artwork.exhibitions.all()
    context = {
        'artwork': artwork,
        'images': images,
        'videos': videos,
        'audio_clips': audio_clips,
        'exhibitions': exhibitions
    }
    return render(request, 'work/artwork_detail.html', context)
