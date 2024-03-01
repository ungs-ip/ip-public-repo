class NASACard:
    def __init__(self, title, description, image_url, date, user=None, id=None):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.date = date
        self.user = user
        self.id = id

    def __str__(self):
        return f'Título: {self.title}, Descripción: {self.description}, URL de la imagen: {self.image_url}, Fecha: {self.date}, Usuario: {self.user}, Id: {self.id}'
    
    # 2 NASACards son iguales si comparten el mismo title, description e image_url.
    # método equals.
    def __eq__(self, other):
        if not isinstance(other, NASACard):
            return False
        return (self.title, self.description, self.image_url) == \
               (other.title, other.description, other.image_url)

    # método hashCode.
    def __hash__(self):
        return hash((self.title, self.description, self.image_url))