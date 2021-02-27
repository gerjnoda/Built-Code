# Built-Code

Programa_Inventario_Servidores

El sistema Programa_Inventario_Servidores esta desarrollado en Python y esta compuesto por un agente que pueda ser ejecutado en cualquier servidor, y recopila los siguientes datos:
● Información sobre el procesador
● Listado de procesos corriendo
● Usuarios con una sesión abierta en el sistema
● Nombre del sistema operativo
● Versión del sistema operativo

A su vez esta compuesta con una API que es una aplicación que permita al agente enviar la información relevada, para que luego, sea almacenada en un .csv con el formato:
<IP de servidor>_<AAAA-MM-DD>.csv

Por ultimo la información es almacenada en formato JSON (archivo de texto plano) que sirve para importarse a una base de datos.
