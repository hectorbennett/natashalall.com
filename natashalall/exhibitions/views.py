from django.shortcuts import render
from django.utils import timezone
from .models import Exhibition
from work.models import Artwork


def index(request):
    exhibitions = Exhibition.objects.filter(
        date__lte=timezone.now()).order_by('date')
    data = {
        'exhibitions': exhibitions
    }
    return render(request, 'exhibitions/index.html', data)


def exhibition_detail(request, pk):
    exhibition = Exhibition.objects.get(pk=pk)
    artworks = Artwork.objects.filter(exhibitions=pk)

    data = {
        'exhibition': exhibition,
        'artworks': artworks
    }
    return render(request, 'exhibitions/exhibition_detail.html', data)
