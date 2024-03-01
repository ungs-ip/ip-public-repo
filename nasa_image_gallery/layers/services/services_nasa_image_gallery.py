# capa de servicio/lógica de negocio

from ..transport import transport
from ..dao import repositories
from ..generic import mapper
from django.contrib.auth import get_user

def getAllImages(input=None):
    json_collection = transport.getAllImages(input)

    images = []

    for object in json_collection:
        nasa_card = mapper.fromRequestIntoNASACard(object)
        images.append(nasa_card)

    return images


def getImagesBySearchInputLike(input):
    return getAllImages(input)


# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = mapper.fromTemplateIntoNASACard(request)
    fav.user = get_user(request)

    return repositories.saveFavourite(fav)


# usados desde el template 'favourites.html'
def getAllFavouritesByUser(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = repositories.getAllFavouritesByUser(user)
        mapped_favourites = []

        for favourite in favourite_list:
            nasa_card = mapper.fromRepositoryIntoNASACard(favourite)
            mapped_favourites.append(nasa_card)

        return mapped_favourites


def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId)