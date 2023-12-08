# ProyectoMultimedia

🔹 Link repositorio -> https://github.com/angelvilla01/ProyectoMultimedia/

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





 
 

  

