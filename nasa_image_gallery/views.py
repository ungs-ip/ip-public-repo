# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services_nasa_image_gallery
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index_page(request):
    return render(request, 'index.html')


def getAllImagesAndFavouriteList(request):
    images = services_nasa_image_gallery.getAllImages()
    favourite_list = services_nasa_image_gallery.getAllFavouritesByUser(request)

    return images, favourite_list


def home(request):
    images, favourite_list = getAllImagesAndFavouriteList(request)
    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list} )


def search(request):
    images, favourite_list = getAllImagesAndFavouriteList(request)
    search_msg = request.POST.get('query', '')

    if (search_msg != ''):
        images_filtered = services_nasa_image_gallery.getImagesBySearchInputLike(search_msg)
        return render(request, 'home.html', {'images': images_filtered, 'favourite_list': favourite_list} )
    else:
        return redirect('home')


@login_required
def getAllFavouritesByUser(request):
    favourite_list = services_nasa_image_gallery.getAllFavouritesByUser(request)
    return render(request, 'favourites.html', {'favourite_list': favourite_list})


@login_required
def saveFavourite(request):
    services_nasa_image_gallery.saveFavourite(request)
    return redirect('home')


@login_required
def deleteFavourite(request):
    services_nasa_image_gallery.deleteFavourite(request)
    return redirect('favoritos')


@login_required
def exit(request):
    logout(request)
    return redirect('home')