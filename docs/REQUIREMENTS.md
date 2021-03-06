# REQUIREMENTS

## Web site

- &#9745;Home con listado de últimos post publicados por usurios.
- &#9745;En `/blogs` mostrar un listado de blogs de usuarios de la plataforma.
- &#9745;En `/blogs/<username>` mostrar blog del usuario con todos los posts del usuario ordenados por el más actual.
- &#9745;En `/blogs/<username>/<post_id>` mostrar detalle del post.
- &#9745;`Post` está compuesto por:
  - title
  - intro
  - body
  - media (opcional)
  - publish_datetime
  - categories (1 o más)
- &#9745;`Category` gestionadas por administrador.
- &#9745;Mismo diseño de posts en home/blog mostrando title, media (si tiene) e intro.
- &#9745;En `/new-post` un formulario para crear un post. Acceden usuarios autenticados. Identificar usuario para publicar POST en su blog.
- &#9745;En `/login` el usuario hará login.
- &#9745;En `/logout` el usuario hará logout.
- &#9745;En `/signup` el usuario se registra con:
  - name
  - surname
  - username
  - email
  - password

## API REST

### API de usuarios

- &#9745;Endpoint de registro con los mismos campos que el formulario de registro.
- &#9745;Endpoint de detalle de usuario, visible para él mismo o administrador.
- &#9745;Endpoint de edición de usuario, usable para él mismo o administrador.
- &#9745;Endpoint de borrado de usuario, usable para él mismo o administrador.

### API de blogs

- &#9745;Endpoint de listado de blogs de la plataforma, con su URL.
  - &#9745;No requiere autenticación.
  - &#9745;Permite búsqueda de blogs por username y ordenación por username.

### API de posts

- &#9745;Endpoint de listado de posts de un blog.
  - &#9745;User no autenticado: solo posts publicados.
  - &#9745;User owner o admin: todos los posts.
  - &#9745;Mostrar title, media, intro y publish_datetime.
  - &#9745;Búsqueda por title o body.
  - &#9745;Ordenar por title o publish_datetime (default descendente).
- &#9745;Endpoint de creación de post para user autenticado, al cual queda vinculado el nuevo post.
- &#9745;Endpoint de detalle de post, con toda la info del post.
  - &#9745;Si no publicado: solo accede owner o admin.
- &#9745;Endpoint de actualización de post solo para owner o admin.
- &#9745;Endpoint de borrado de post solo para owner o admin

## Extras

### General

- &#9744;Añadir filtros post por categorias al admin Django.
- &#9744;Mostrar mismas columnas en listado que datos de listado API.
- &#9745;Personalizar página de detalle del post.

### Webpage

- &#9744;Darle diseño a la página.
- &#9744;Filtrado por categorias en blog de usuario.
- &#9744;Paginar post en el blog de usuario.

### API Rest

- &#9744;Endpoint de subida de archivos para media de posts.
- &#9744;Filtrado por categorias en listado de posts.
- &#9744;Mostrar número de posts de cada blog, en la api de blog.
- &#9744;Mostrar author (name+surname) en el endpoint de listado y detalle de posts de un blog.