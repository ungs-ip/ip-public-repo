from nasa_image_gallery.config import config

def version(request):
    return {'VERSION': config.VERSION} 