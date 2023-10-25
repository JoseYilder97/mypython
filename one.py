#importa el módulo  time
import time
#defino una funcion
def simular_reloj():
    #Inicalizo la las variables horas, minutos segundos en 0
    horas = 0
    minutos = 0
    segundos = 0
#utilizo el bucle while con horas  < 24
    while horas < 24:
        print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
        time.sleep(1)
        segundos += 1
#Esta línea reinicia el valor de la variable  segundos  a 0. Al llegar a 60 segundos
        if segundos == 60:
            segundos = 0
            minutos += 1
# Esta línea incrementa el valor de la variable  minutos  en 1. Al llegar a 60 segundos y reiniciar  segundos
        if minutos == 60:
            minutos = 0
            horas += 1
#llamo la funcion
simular_reloj()