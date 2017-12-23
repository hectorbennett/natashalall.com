from django.shortcuts import render
from django.utils import timezone
from .models import Artwork


def index(request):
    artworks = Artwork.objects.filter(
        creation_date__lte=timezone.now()).order_by('creation_date')
    return render(request, 'work/index.html', {'artworks': artworks})


def artwork_detail(request, pk):
    artwork = Artwork.objects.get(pk=pk)
    return render(request, 'work/artwork_detail.html', {'artwork': artwork})
