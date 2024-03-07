from django.db import models
from django.conf import settings

# modelo para un favorito.
# un usuario puede tener 0...n favoritos asociados. Si un usuario es borrado, no nos interesa retener sus favoritos, por lo cual se borran en cascada.
class Favourite(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.TextField()
    date = models.DateField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # asociamos el favorito con el usuario en cuestión.

    class Meta:
        unique_together = ('user', 'title', 'description', 'image_url', 'date')