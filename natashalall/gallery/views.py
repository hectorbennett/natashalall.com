from django.shortcuts import render
from .models import Artwork
# Create your views here.

def work(request):
    Artworks = Artwork.objects.filter(
        date_created__lte=timezone.now()).order_by('date_created')
    return render(request, 'main/work.html', {'Artworks': Artworks})
