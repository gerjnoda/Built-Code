# Programa_Inventario_Servidores

Programa_Inventario_Servidores está desarrollado en Python y está compuesto por un agente que pueda ser ejecutado en cualquier servidor, y recopila los siguientes datos:
● Información sobre el procesador
● Listado de procesos corriendo
● Usuarios con una sesión abierta en el sistema
● Nombre del sistema operativo
● Versión del sistema operativo

A su vez está compuesta con una API que es una aplicación que permita al agente enviar la información relevada, para que luego, sea almacenada en un .csv con el formato:
<IP de servidor>_<AAAA-MM-DD>.csv

Por último la información es almacenada en formato JSON (archivo de texto plano) que sirve para importarse a una base de datos.

# Instalación
Para ejecutar es requerido tener instalado python (https://www.python.org/) en servidor donde se vaya a ejecutar

El programa usa las librerías: psutil (https://pypi.org/project/psutil/), sockets (https://pypi.org/project/sockets/) y pandas (https://pypi.org/project/pandas/). Por lo tanto, para que funcione es necesario tener instalado los siguientes paquetes:
1. psutil
C:\>python -m pip install psutil

2. pandas
pip install pandas

3. sockets
pip install sockets

Seguramente deban instalar o actualizar la librería pip para poder instalar las librerías
C:\python -m pip install --upgrade pip

# Configuración
Actualmente no es necesario cambiar La configuración del programa; pero se debe indicar el directorio al momento de la ejecución del programa por línea de comando

NOTA: En una siguiente versión se puede incluir como mejora la ruta especifica del directorio donde se genere el documento csv ó json.

# Funcionamiento
1. El programa hace el relevamiento de la información del servidor
2. Determina información complementaria para identificar el servidor (dirección IP) y fecha al momento de la ejecución.
3. La información recopilada es almacenada en formato csv
4. Por último la información es almacenada en formato json desde csv



