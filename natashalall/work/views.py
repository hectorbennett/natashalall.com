from django.shortcuts import render
from django.utils import timezone
from .models import Artwork



def index(request):
    artworks = Artwork.objects.filter(
        creation_date__lte=timezone.now()).order_by('creation_date')
    data = {
        'artworks': artworks,
    }
    return render(request, 'work/index.html', data)


def artwork_detail(request, pk):
    artwork = Artwork.objects.get(pk=pk)
    images = artwork.images.all().filter(visible=1)
    videos = artwork.videos.all()
    data_dict = {'artwork': artwork, 'images': images, 'videos': videos}
    return render(request, 'work/artwork_detail.html', data_dict)
