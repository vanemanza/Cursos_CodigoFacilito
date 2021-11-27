Docker:
plataforma para implementar aplicaciones atraves de unidades estandarizadas llamadas contenedores.

IMAGENES:
Haciendo una analogía con POO, una imagen podría compararse a una CLASE, donde definimos todas las configuraciones q queremos q tenga nuestro objeto.
Por ej q tenga instalado NGINX.
A traves de una imagen, podemos instanciar a multiples objetos (contenedores)

IMAGEN == CLASE
CONTENEDOR == INSTANCIA DE LA IMAGEN

Contenedor:
Es una instancia de una imagen, que ejecuta todas las instrucciones definidas en las mismas.

(Es un lugar virtual donde almacenar dependencias, que una app necesita para poder ejecutarse
correctamente.
A traves de un contenedor, podemos empaquetar una aplicación con todo lo necesario (runtimes?, bibliotecas, entre otros componentes) y ejecutarla en cualquier parte donde estemos ejecutando Docker, ya sea en nuetra máquina local o en un servidor.
Esto garantiza q la aplicacion se ejecuta de la misma manera, tanto en desarrollo como en producción, como en diferentes sistemas operativos.)

Docker hub:

Registro donde podemos descargar y subir imagenes.
Sería como Github pero para imagenes de Docker. 
en hu.docker.com puedo encontrar multiples imagenes, para MyQSL, Postgres, Ubuntu, etc

COMO FUNCIONA DOCKER:
Funciona a traves de una arquitectura cliente-servidor.
* El servidor es el encargado de la administracion de imagenes y contenedores --> Docker Engine
* El cliente que puede ser el id? de comandos? o un cliente grafico, que se conecta al servidor a traves de una API.

CLIENTE -- pedimos q ejecute nuestra imagen de UBUNTU -> SERVIDOR  -- descarga la imagen y la ejecuta en nuestro host --> REGISTRO PUBLICO (Ducker hub)

______________________________________________________







