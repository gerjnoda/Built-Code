# Built-Code

**Programa_Inventario_Servidores**

Programa_Inventario_Servidores esta desarrollado en Python y esta compuesto por un agente que pueda ser ejecutado en cualquier servidor, y recopila los siguientes datos:
● Información sobre el procesador
● Listado de procesos corriendo
● Usuarios con una sesión abierta en el sistema
● Nombre del sistema operativo
● Versión del sistema operativo

A su vez esta compuesta con una API que es una aplicación que permita al agente enviar la información relevada, para que luego, sea almacenada en un .csv con el formato:
<IP de servidor>_<AAAA-MM-DD>.csv

Por ultimo la información es almacenada en formato JSON (archivo de texto plano) que sirve para importarse a una base de datos.

**Instalación**
Para ejecutar el programa usa las librerias: psutil (https://pypi.org/project/psutil/) y pandas (https://pypi.org/project/pandas/). Por lo tanto, para que funcione es necesario tener instalado los siguientes paquetes:
1. psutil
C:\>python -m pip install psutil

2. pandas
pip install pandas

Seguramente deban instalar o actualizar la libreria pip para poder istalar las librerias
C:\python -m pip install --upgrade pip

**Cofiguración**
Actualmente no es necesario cambiar La configuración del programa; pero se debe indicar el directorio al momento de la ejecución del programa por linea de comando

NOTA: En una siguiete versión se puede incluir como mejora la ruta especifica del directorio donde se genere el documento csv ó json.



