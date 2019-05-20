from django.shortcuts import render ,get_object_or_404,redirect

# Create your views here.
from .models import Photo
from django.views import generic
from .forms import PhotoForm

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/index.html', {'photos': photos})

def photo_detail(request, pk):
    photos = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photos':photos})


def photo_create(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo:list')
    else:
        form = PhotoForm()
    return render(request, 'photo/photo_create.html', {
        'form': form,
    })
