from django.shortcuts import render
from django.utils import timezone
from .models import Artwork


def index(request):
    artworks = Artwork.objects.filter(
        creation_date__lte=timezone.now()).order_by('creation_date')
    return render(request, 'work/index.html', {'artworks': artworks})
