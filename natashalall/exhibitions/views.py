from django.shortcuts import render
from django.utils import timezone
from .models import Exhibition
from work.models import Artwork


def index(request):
    exhibitions = Exhibition.objects.all()
    context = {'exhibitions': exhibitions}
    return render(request, 'exhibitions/index.html', context)


def exhibition_detail(request, pk):
    exhibition = Exhibition.objects.get(pk=pk)
    artworks = Artwork.objects.filter(exhibitions=pk)
    context = {'exhibition': exhibition, 'artworks': artworks}
    return render(request, 'exhibitions/exhibition_detail.html', context)
