from django.shortcuts import render ,get_object_or_404

# Create your views here.
from .models import Photo
from django.views import generic

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/index.html', {'photos': photos})

def photo_detail(request, pk):
    photos = get_object_or_404(Photo, pk=pk)
    return render(request, 'shop/photo_detail.html', {'photos':photos})

