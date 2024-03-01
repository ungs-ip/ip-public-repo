# mapper: se refiere a un componente o conjunto de funciones que se utiliza para convertir o "mapear" datos de un formato o estructura a otro. Esta conversión se realiza típicamente cuando se trabaja con diferentes capas de una aplicación, como por ejemplo, entre la capa de datos y la capa de presentación, o entre dos modelos de datos diferentes, mejorando la coherencia y eficiencia.

from nasa_image_gallery.layers.generic.nasa_card import NASACard

# usado cuando la info. viene de la API de la nasa, para transformarlo en una NASACard.
def fromRequestIntoNASACard(object):
    nasa_card = NASACard(
                        title=object['data'][0]['title'],
                        description=object['data'][0]['description'], 
                        image_url=object['links'][0]['href'], 
                        date=object['data'][0]['date_created'][:10]
                )

    return nasa_card


# usado cuando la info. viene del template, para transformarlo en una NASACard antes de guardarlo en la base de datos.
def fromTemplateIntoNASACard(templ): 
    nasa_card = NASACard(
                        title=templ.POST.get("title"),
                        description=templ.POST.get("description"),
                        image_url=templ.POST.get("image_url"),
                        date=templ.POST.get("date")
                )
    return nasa_card


# cuando la info. viene de la base de datos, para transformarlo en una NASACard antes de mostrarlo.
def fromRepositoryIntoNASACard(repo_dict):
    nasa_card = NASACard(
                        id=repo_dict['id'],
                        title=repo_dict['title'],
                        description=repo_dict['description'],
                        image_url=repo_dict['image_url'],
                        date=repo_dict['date'],
                )
    return nasa_card