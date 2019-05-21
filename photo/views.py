from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Photo
from django.views import generic
from .forms import PhotoForm,PhotoUpdateForm


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/index.html', {'photos': photos})


def photo_detail(request, pk):
    photos = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photos': photos})


def photo_create(request, photo=None):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)  # instance는 모델폼에서 지원
        if form.is_valid():
            photo = form.save()
            return redirect(photo)
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'photo/photo_create.html', {
        'form': form,
    })


# def photo_update(requset,pk):
#     photo = get_object_or_404(Photo, pk=pk)
#     return photo_create(requset, photo)

def photo_update(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        form = PhotoUpdateForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
        return redirect('photo:list')
    else:
        form = PhotoUpdateForm(instance=photo)
    return render(request, 'photo/photo_update.html', {
        'form': form, })
