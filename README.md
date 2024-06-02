# FileTransform

##	Descripción General
Este proyecto consiste en una aplicación web desarrollada con Flask, un framework minimalista de Python. Durante esta memoria explicaremos el proceso de realización de la aplicación que procesa y convierte los ficheros de una forma sencilla.
Primero, procederemos a analizar los requisitos que conforman la aplicación y el porqué se han tomado las decisiones de diseño. A continuación, explicaremos que tecnologías hemos usado y como se ha realizado la implementación de estas. Terminaremos con un manual de usuario para poder ejecutar la aplicación sin complicaciones.
Para llevar a cabo el desarrollo, se ha programado una aplicación en Python usando Flask con la finalidad realizar conversiones de ficheros y compresión de vídeo.  Para la conversión de ficheros se han utilizado librerías externas y para la compresión de vídeo nos hemos apoyado en el uso del software FFmpeg.
##	Requisitos de la aplicación

La aplicación cumple con los siguientes requisitos:
- Compresión de vídeo en formato MP4: permite comprimir el vídeo proporcionado un tamaño de 640 x 360 píxeles utilizando el códec de vídeo libx264 y para la parte del audio usamos el códec AAC, con ello buscamos un equilibrio entre calidad y peso del fichero.
-	Conversión de Pdf a Word: permite convertir un archivo con formato pdf a Word mediante el uso de la librería pdf2docx.
-	Conversión de JPG a WebP: nos permite convertir un archivo con formato JPG a WebP, para ello hacemos uso de la librería PIL.
-	Conversión de JPG a PNG: Permite la conversión de imágenes JPG a PNG. Esta función es útil cuando se requiere transparencia o una mejor calidad de imagen en archivos no comprimidos.



## DECISIONES Y JUSTIFICACIÓN DEL DISEÑO

En primer lugar, tenemos el componente principal en el cual tenemos los cuatro tipos de compresión que se han explicado en los requisitos de la aplicación.
En la parte superior de se puede navegar de un componente al otro dándole usabilidad a la aplicación web.

<br>


 ![image](https://github.com/angelvilla01/ProyectoMultimedia/assets/72606604/864ce6f4-55a6-457f-91ce-14ae6f18243d)

<br>



En los diferentes componenteste permite cargar los archivos arrastrando o haciendo clic y buscándolo en tu ordenador. Una vez que esté subido el archivo debemos pulsar el botón subir para que se comience la descarga.
Una vez que se está comprimiendo aparecerá una barra en la cual te indicará el porcentaje por el que va la compresión.
Por último, para descargar el fichero, el botón de descarga no se habilita hasta que el archivo ha sido procesado. Una vez descargado después de 15 segundos el componente se reinica para poder volver a comprimir otro nuevo archivo. Esto se replica en todos los componentes.

<br>


![image](https://github.com/angelvilla01/ProyectoMultimedia/assets/72606604/2b5b8bbd-cde8-4391-9a95-82b1c4ccd138)

## Manual de Usuario

Para poder ejecutar el proyecto es importante seguir las siguientes instrucciones, pero antes, vamos a comentar los requisitos.
Requisitos:
1.	Instalar <b>Python 3.12.0</b>
2.	Ejecutar en el CMD (símbolo del sistema) en modo administrador. ¿Por qué en modo administrador? -> suele dar error al instalar nuevos paquetes en Python al no tener permiso.
a.	Nos dirigimos mediante el comando “cd” al directorio donde esté el proyecto y ejecutamos “python instalador.py”, nos instalará todos los paquetes/librerías necesarias.
3.	Para poder usar el componente de compresor de vídeo, necesitamos extraer del .zip proporcionado el FFMPEG, lo más sencillo es extraer la carpeta en el disco C. Posteriormente en las variables de entorno del sistema, como se indica a continuación añadiremos la ruta de la carpeta (/bin) para que pueda ser detectada por el sistema.

![image](https://github.com/angelvilla01/ProyectoMultimedia/assets/47080025/48a56992-0f61-4436-b7ca-2d0bccb931c9)

<b>Ejecución</b>: <br>
🔹	Recomendable: ejecutarlo en visual studio code mediante la terminal con el comando:  `python app.py` <br>
🔹	Una vez ejecutado accederemos a la dirección:	`http://127.0.0.1:5000` <br>
🔹 En la terminal también se indica la dirección


 
 

  

