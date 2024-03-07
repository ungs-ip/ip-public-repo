# capa DAO de acceso/persistencia de datos.

from nasa_image_gallery.models import Favourite

def saveFavourite(image):
    try:
        fav = Favourite.objects.create(title=image.title, description=image.description, image_url=image.image_url, date=image.date, user=image.user)
        return fav
    except Exception as e:
        print(f"Error al guardar el favorito: {e}")
        return None

def getAllFavouritesByUser(user):
    favouriteList = Favourite.objects.filter(user=user).values('id', 'title', 'description', 'image_url', 'date')
    return list(favouriteList)

def deleteFavourite(id):
    try:
        favourite = Favourite.objects.get(id=id)
        favourite.delete()
        return True
    except Favourite.DoesNotExist:
        print(f"El favorito con ID {id} no existe.")
        return False
    except Exception as e:
        print(f"Error al eliminar el favorito: {e}")
        return False