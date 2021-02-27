# Secuecia para obtener iformación de plataforma
import platform as pl

datos_servidor = [
                'processor',
                'system',
                'version'
    ]
    
for perfil in datos_servidor:
        if hasattr(pl,perfil):
            print('%s: %s' % (perfil,getattr(pl,perfil)())
            )
#Secuecia para obtener el usuario  
import getpass
print (getpass.getuser())

#Secuecia para obtener la direción IP
import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(ip)

#Secuecia para obtener los procesos
import psutil
for p in psutil.process_iter():
    print(p, p.name(), p.pid)

#Secuecia para obtener la fecha
import pandas as pd
import datetime
current_date = datetime.datetime.now()

#Secuecia para compilar en variables en documeto csv
import csv
hostnamev = [hostname]
ipv = [ip]
userv = [getpass.getuser()]
systemv = [pl.system()]
processorv = [pl.processor()]
versionv = [pl.version()]
count = 0

#Secuecia para crear nombre documeto csv
name = str(socket.gethostbyname(hostname))+datetime.datetime.now().strftime('-%Y-%m-%d')
filename = "%s.csv" % name 

#Secuecia para crear documeto csv
with open(filename,'w',newline='') as csvfile:
    fieldnames = ['system','processor','version','hostname','ip','user','proceso']
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    thewriter.writeheader()

    for p in psutil.process_iter():
        procesosv = (p.name(), p.pid, p)
        thewriter.writerow({'system':systemv,'processor':processorv,'version':versionv,'hostname':hostnamev,'ip':ipv,'user':userv,'proceso':procesosv})
        count += 1

#Secuecia para crear documeto json
import csv
import json
import pandas as pd 
with open("archivo_plano.json", "w") as archivo:
    archivo.write("")
    archivo.close()
pasar = pd.DataFrame(pd.read_csv(filename, sep = ",", header = 0, index_col = False))
pasar.to_json("archivo_plano.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
