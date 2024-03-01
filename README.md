# Introducción a la Programación - primer semestre del 2024.
## Trabajo práctico: galería de imágenes de la NASA 🚀


![Galería de Imágenes de la NASA](https://api.nasa.gov/assets/img/general/apod.jpg)

### Introducción
- El trabajo consiste en implementar una aplicación web *fullstack* usando **[Django Framework](https://docs.djangoproject.com/en/4.2/)** que permita consultar las imágenes de la API pública que proporciona la NASA. La información que provenga de esta API será renderizada por el *framework* en distintas *cards* que mostrarán -como mínimo- la imagen en cuestión, un título y una descripción. Adicionalmente -y para enriquecerla- se prevee que los estudiantes desarrollen la lógica necesaria para hacer funcionar el buscador central y un módulo de autenticación básica (usuario/contraseña) para almacenar uno o más resultados como **favoritos**, que luego podrán ser consultados por el usuario al loguearse. En este último, la app deberá tener la lógica suficiente para verificar cuándo una imagen fue marcada en favoritos.

- Gran parte de la aplicación ya está resuelta: solo falta implementar las funcionalidades más importantes 😉.

### ¿Cómo empiezo?

1. Instalá Python desde ```www.python.org```. Asegúrate de agregarlo al PATH durante la instalación.

2. Cloná el repositorio en tu computadora:
```git clone X```

3. Dentro de la carpeta del repositorio, abrir una terminal de *VS Code* e instalar Django ejecutando el siguiente comando:
```pip install django=4.2.10```

4. Instalá las dependencias necesarias:
```pip install -r requirements.txt```

5. Ejecutá el servidor Django (3000 representa el puerto donde se ejecutará la app):
```python manage.py runserver 3000```

6. Abrí tu navegador y dirigíte a ```http://localhost:3000``` para ver la aplicación. Deberá mostrar una pantalla como la siguiente: 
![imagen](https://i.ibb.co/GFJdgHr/galeria-default.png)

7. Por último, para ver el contenido de la base integrada (SQLite), recomendamos el uso de **DB Browser for SQLite**. Link de descarga: https://sqlitebrowser.org/dl/
    - El archivo que se debe abrir es **db.sqlite3**.

### Lo que ya está implementado
- A nivel **template**, se cuenta con 4 HTMLs: **header (cabecera de la página)**, **footer (pie de página)**, **home (sección donde se mostrarán las imágenes y el buscador)** e **index (contener principal que incluye a los 3 HTMLs anteriores).** Para el caso del *header*, se implementó cierta lógica para determinar si un usuario está logueado (o no) y obtener así su nombre; para el caso del *home*, éste tiene un algoritmo que permite recorrer cada objeto de la API y dibujar su información en pantalla. El *footer* no posee acciones a nivel código relevantes para el desarrollo.

- A nivel **views**, en el archivo **views.py** encontrarán algunas funciones semidesarrolladas: *index_page(request)* que renderiza el contenido de 'index.html'; *home(request)* que obtiene todas las imágenes mapeadas de la API -a través de la capa de servicio- y los favoritos del usuario, y muestra el contenido de 'home.html' pasándole dicha información. Esta última hace uso de la función auxiliar *getAllImagesAndFavouriteList(request)* que devuelve 2 listas: una de las imágenes de la API y otra de las imágenes marcadas como favoritos del usuario.

- A nivel **lógica**, se incluye el archivo **transport.py** completo con todo el código necesario para consumir la API. Además, se anexa un **mapper.py** con la lógica necesaria para convertir/mapear los resultados en una **NASACard** (objeto que finalmente se utilizará en el template para dibujar los resultados).

- El proyecto está construido sobre una **[arquitectura multicapas](https://medium.com/@e0324913/multilayered-software-architecture-1eaa97b8f49e)**, donde cada capa posee una única responsabilidad y se encuentra desacoplada del resto. Son las siguientes:
    - **DAO** (empleada para el alta/baja/modificación -CRUD/ABM- de objetos en una base de datos integrada, llamada **[SQLite](X)**).
    - **Services** (usada para la lógica de negocio de la aplicación).
    - **Transport** (utilizada para el consumo de la API en cuestión).

Si bien no es un parámetro de evaluación dónde colocan las funciones, es altamente recomendado que las funciones que se agreguen estén en las capas que correspondan (consultar con los docentes en caso de dudas).

### ¿Qué voy a ver al iniciar la app?
- Al iniciar la aplicación y hacer clic sobre **Galería**, verás lo siguiente:
![imagen](https://i.ibb.co/bN6bhVG/galeria-1.png)


### Lo que falta hacer

- Aún faltan implementar ciertas funciones de los archivos **views.py** y **services_nasa_image_gallery.py**. Éstas son las encargadas de hacer que las imágenes de la galería se muestren/rendericen:
    
    - **views.py**:
        - *home(request):* invoca a getAllImagesAndFavouriteList(request) para obtener 2 listados que utilizará para renderizar el template.
        ![imagen](https://i.ibb.co/0mMLRrv/galeria-4.png)
        - *getAllImagesAndFavouriteList(request):* invoca al servicio correspondiente para obtener 2 listados, uno de las imágenes de la API y otro -si corresponde- de los favoritos del usuario.
        ![imagen](https://i.ibb.co/DpRXXj5/galeria-4.png)


    - **services_nasa_image_gallery.py**:
        - *getAllImages(input=None):* obtiene un listado de imágenes de la API. El parámetro *input*, si está presente, indica sobre qué imágenes debe filtrar/traer.
        ![imagen](https://i.ibb.co/mqGRNfR/galeria-3.png)

**Concluido su desarrollo, deberían ver algo como lo siguiente:**
![imagen](https://i.ibb.co/yptbG3g/galeria-2.png)

### Condiciones de entrega

- Requisitos de aprobación y criterio de corrección
    - El TP debe realizarse en grupos de 2 o 3 integrantes (no 1). Para aprobar el trabajo se deberán reunir los siguientes ítems:
      - La galería de imágenes se muestra adecuadamente (**imagen**, **título** y **descripción**).
      - El código debe ser **claro**. Las variables y funciones deben tener nombres que hagan fácil de entender el código a quien lo lea -de ser necesario, incluir comentarios que clarifiquen-. **Reutilizar el código mediante funciones todas las veces que se amerite.**
      - No deben haber variables que no se usan, funciones que tomen parámetros que no necesitan, ciclos innecesarios, etc.
    - **El 'correcto' funcionamiento del código NO es suficiente para la aprobación del TP, son necesarios todos los ítems mencionados arriba.**



### Opcionales
Las siguientes funcionalidades del juego NO son necesarias para la aprobación (con nota mínima), pero sirven para mejorar la nota del trabajo. De optar por hacerlas, se aplican las mismas reglas y criterios de corrección que para las funcionalidades básicas. Cualquier otra funcionalidad extra que se desee implementar debe ser antes consultada con los docentes.

- **Favoritos** ⭐
  - [explicación]
 
- **Buscador** ⭐
  - [explicación]
 
- **Inicio de sesión** ⭐
  - [explicación]

- Paginación de resultados para evitar desplazamiento vertical // en su defecto, **infinite scroll** (estilo Instagram ó Facebook).
  - [explicación]

- Comentarios a las imágenes favoritas
  - [explicación]
  
- ALTA de nuevos usuarios*
  - [explicación]

- Servicio de notificación por correo electrónico para nuevas altas de usuarios (depende de *)
  - [explicación] 

- Internacionalización (i18n) de la aplicación con soporte para múltiples idiomas
  - [explicación] 

- Implementación de **pruebas unitarias** para el algoritmo de búsqueda de imágenes
  - [explicación]
   
- Caché para búsqueda rápida de resultados
  - [explicación]
   
- *Loading Spinner* para la carga de imágenes
  - [explicación]

- Eliminar resultado de búsqueda no agradable (botón 'no mostrar esta img')
  - [explicación]
  
- Cambiar CSS/estilos de las páginas
  - [explicación]

### Fecha de entrega
El trabajo debe ser entregado en la fecha estipulada en el cronograma. **Recordar que es requisito hacer pre-entregas.**

### Forma de entrega
- **Código:** se entregará mediante *Pull Request* al repositorio desde el cual clonaron el proyecto. **Deben escoger a un integrante** que se encargue de ejecutarlo, teniendo especial cuidado de seleccionar el **branch/rama** adecuado ANTES de su envío (si hubo un error, cancelar la solicitud y volverla a enviar). 
- **Informe:** deben redactar un documento donde exista una introducción que explique de qué se trata el trabajo (sin utilizar lenguaje técnico), que incluya el código de las funciones implementadas y una breve explicación de cada una de ellas junto con las **dificultades de implementación** y **decisiones tomadas** -con su correspondiente justificación-. **NO incluir explicaciones de funcionalidades de Python, Django o similares**. Este documento debe estar en formato PDF anexo dentro de la carpeta del TP (se entrega junto al *Pull Request* del punto anterior).
    
 Encontrarán un video explicativo ingresando en el siguiente link: X


### Documentación adicional
- Documentación oficial de Django disponible aquí: https://docs.djangoproject.com/en/4.2/
