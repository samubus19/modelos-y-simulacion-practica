import datetime
import random
import pandas as pd
from tabulate import tabulate
class Sistema():
    
    #* Inicializacion de variables
    def __init__(self) -> None:
        self.cola                      = 0 #La cola siempre inicia en 0
        self.ps                        = int(input("Ingrese Valor de PS inicial:"))
        self.data                      = []
        hora_actual_input              = (input("Ingrese hora actual inicial (h:m:s):")).split(sep=":") #9:0:32
        hora_llegada_cliente_input     = (input("Ingrese hora llegda cliente inicial (h:m:s):")).split(sep=":") #9:0:49
        hora_fin_serivicio_input       = (input("Ingrese hora fin servicio inicial (h:m:s):")).split(sep=":") #9:01:07
        
        self.hora_actual               = datetime.datetime(year   = datetime.date.today().year, 
                                                           month  = datetime.date.today().month, 
                                                           day    = datetime.date.today().day, 
                                                           hour   = int(hora_actual_input[0]), 
                                                           minute = int(hora_actual_input[1]), 
                                                           second = int(hora_actual_input[2]))
         
        self.hora_llegada_cliente      = datetime.datetime(year   = datetime.date.today().year, 
                                                           month  = datetime.date.today().month, 
                                                           day    = datetime.date.today().day, 
                                                           hour   = int(hora_llegada_cliente_input[0]), 
                                                           minute = int(hora_llegada_cliente_input[1]), 
                                                           second = int(hora_llegada_cliente_input[2]))
         
        self.hora_fin_servicio         = datetime.datetime(year   = datetime.date.today().year, 
                                                           month  = datetime.date.today().month, 
                                                           day    = datetime.date.today().day, 
                                                           hour   = int(hora_fin_serivicio_input[0]), 
                                                           minute = int(hora_fin_serivicio_input[1]), 
                                                           second = int(hora_fin_serivicio_input[2]))
         
        self.hora_abandono_de_cola     = datetime.datetime(year   = datetime.date.today().year, 
                                                           month  = datetime.date.today().month, 
                                                           day    = datetime.date.today().day, 
                                                           hour   = 23, 
                                                           minute = 3, 
                                                           second = 0)
        
        self.tiempo_abandono_cliente   = datetime.timedelta(minutes=random.randint(int(input("Ingrese rango minimo de tiempo de abandono de cliente (minutos):")), int(input("Ingrese rango maximo de tiempo de abandono de cliente (minutos):"))))
        
        self.tiempo_de_llegada_minimo  = int(input("Ingrese valor minimo de tiempo de llegada del cliente (segundos):"))#10 #tiempo en segundos
        self.tiempo_de_llegada_maximo  = int(input("Ingrese valor maximo de tiempo de llegada del cliente (segundos):"))#10 #tiempo en segundos
        self.tiempo_de_servicio_minimo = int(input("Ingrese valor minimo de duracion del servicio (segundos):"))#50 #tiempo en segundos
        self.tiempo_de_servicio_maximo = int(input("Ingrese valor maximo de duracion del servicio (segundos):"))#50 #tiempo en segundos
        
        self.horas_abandono            = []
        
        #variables auxiliares
        self.aux_hora_fin_servicio     = False
        
    def abandono_de_cola(self):
        self.hora_actual = self.hora_abandono_de_cola
        self.cola       -= 1
        if(len(self.horas_abandono) > 0):
            self.horas_abandono.remove(self.horas_abandono[0])
        self.hora_abandono_de_cola = self.horas_abandono[0]
        
    #* Metodo para simular evento de la entrada de un cliente al sistema
    def llegada_cliente_al_sistema(self):
        self.hora_actual               = self.hora_llegada_cliente
        if self.ps == 0:
            self.ps                    = 1 
            self.hora_fin_servicio     =  self.hora_llegada_cliente + self.duracion_servicio
            self.aux_hora_fin_servicio = False
        else:
            self.horas_abandono.append(self.hora_llegada_cliente + self.tiempo_abandono_cliente)
            self.cola                 += 1
            self.hora_abandono_de_cola = self.horas_abandono[0]
        
        self.hora_llegada_cliente     += self.intervalo_por_cliente

    #* Metddo para simular evento de la salida de un cliente al sistema
    def fin_de_servicio(self):
        self.hora_actual               = self.hora_fin_servicio
        self.ps = 0
        if(self.cola > 0):
            self.ps                    = 1
            self.cola                 -= 1
            self.hora_fin_servicio     = self.hora_actual + self.duracion_servicio
            self.horas_abandono.remove(self.horas_abandono[0])
            if(len(self.horas_abandono) > 0):
                self.hora_abandono_de_cola = self.horas_abandono[0]
        else:
            self.hora_fin_servicio    += datetime.timedelta(hours=5)
            self.aux_hora_fin_servicio = True
            
            
    def convertir_tipo_fecha(self, fecha):
        if(isinstance(fecha, datetime.datetime)):
            return fecha.time()
        return fecha

    #* Metodo para elegir el evento que se va a simular
    def elegirEvento(self):
        
        for i in range(0,10):
            
            self.duracion_servicio     = datetime.timedelta(seconds=random.randint(self.tiempo_de_servicio_minimo,self.tiempo_de_servicio_maximo))
            self.intervalo_por_cliente = datetime.timedelta(seconds=random.randint(self.tiempo_de_llegada_minimo, self.tiempo_de_llegada_maximo))
            
            hora_fin_servicio_aux      = ('--------' if self.aux_hora_fin_servicio else self.convertir_tipo_fecha(self.hora_fin_servicio))
            
            
            self.data.append([self.convertir_tipo_fecha(self.hora_actual),
                      self.convertir_tipo_fecha(self.hora_llegada_cliente),
                      hora_fin_servicio_aux,
                      self.convertir_tipo_fecha(self.hora_abandono_de_cola),
                      self.cola,
                      self.ps,
                      self.tiempo_abandono_cliente.seconds,
                      [list(sorted(set(self.horas_abandono)))]])
            
            if len(self.data) > 0:
                for x in self.data:
                    for j in x[7]:
                        for k in range(len(j)):
                            j[k] = self.convertir_tipo_fecha(j[k])
            
            if(self.hora_llegada_cliente <= self.hora_fin_servicio and self.hora_llegada_cliente <= self.hora_abandono_de_cola):
                self.llegada_cliente_al_sistema()
            elif(self.hora_fin_servicio <= self.hora_abandono_de_cola):
                self.fin_de_servicio()
            else:
                self.abandono_de_cola()
            
        print(pd.DataFrame(data=self.data, columns=['|Hs Actual', 
                                                    '|Hs prox cliente', 
                                                    '|Hs fin serv', 
                                                    '|Hs abandono cola',
                                                    '|Q', 
                                                    '|PS', 
                                                    '|Tiempo abandono de cola',
                                                    '|Horas abandono de cola']))


##Instancio la clase del sistema    
sistema = Sistema()
sistema.elegirEvento()

