# Entrega_final_blog

### Acerca del Blog  

El proyecto trata de un blog dedicado a recomendaciones y experiencias de los miembros sobre sus experiencias en lavaderos que hayan asistido.
Los usuarios podrán observar la lista de los posteos, pero para observar el detalle, **modificar**, **crear** o **eliminar** contenido deberán estar **logueados** o en su defecto, **registrarse**.  
Cada **post** consta de un nombre del lavadero, título, contenido, autor, su localidad/ciudad y fecha de publicación (que se agrega automáticamente).  
Los posts se listan del más reciente al más antiguo.  

Cada **usuario** puede editar su perfil y agregar una imágen como avatar.  
Cada usuario consta de un numbre de usuario, contraseña y un email como datos obligatorios, y si así lo desean pueden agregar su nombre y apellido.  
En el perfil del usuario se lista además la fecha de su último ingreso y la fecha en la que se ha unido (registrado) al blog.  

Los datos de guardan en una base de datos de motor SQLite ya provisto por Django.  

#### Mensajería
Los usuarios cuentan con un sistema de mensajería a modo de mensaje directo.  
Los mensajes sólo los pueden ver los usuarios a los cuales están destinados y el usuario que envió el mismo.  
Dentro del perfil o desde la barra de navegación el usuario accederá a su **Inbox** donde verá su bandeja de entrada y su bandeja de salida.  
  
#### Layout
El blog cuenta con una **barra de navegación** a la cual se puede acceder a las distintas secciones del mismo. (Home, Posts y About).  
Además en el margen derecho podrás ingresar o crear un usuario.  
Al estar logueado en el margen derecho se muestra el nombre de usuario, y avatar, con un menú desplegable donde se puede acceder al Perfil, a sus mensajes y cerrar la sesión.


***
### Video explicativo

https://youtu.be/j265t_3qB9o