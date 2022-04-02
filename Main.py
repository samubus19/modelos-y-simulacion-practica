import datetime
import random
import pandas as pd
class Sistema():
    
    #* Inicializacion de variables
    def __init__(self, cola, ps, hora_actual_inicial, hora_llegada_cliente_inicial, hora_fin_servicio_inicial, iteraciones, duracion_servicio_min, duracion_servicio_max, intervalo_cliente_min, intervalo_cliente_max):
        self.iteraciones           = iteraciones
        self.cola                  = cola
        self.ps                    = ps
        self.data                  = []
        self.hora_actual           = datetime.datetime(2022, 6, 22, int(hora_actual_inicial[0]), int(hora_actual_inicial[1]), int(hora_actual_inicial[2]))
        self.hora_llegada_cliente  = datetime.datetime(2022, 6, 22, int(hora_llegada_cliente_inicial[0]), int(hora_llegada_cliente_inicial[1]), int(hora_llegada_cliente_inicial[2]))
        self.hora_fin_servicio     = datetime.datetime(2022, 6, 22, int(hora_fin_servicio_inicial[0]), int(hora_fin_servicio_inicial[1]), int(hora_fin_servicio_inicial[2]))
        self.duracion_servicio_min = duracion_servicio_min
        self.duracion_servicio_max = duracion_servicio_max
        self.intervalo_cliente_min = intervalo_cliente_min
        self.intervalo_cliente_max = intervalo_cliente_max
        # self.duracion_servicio     = datetime.timedelta(seconds=duracion_servicio)
        # self.intervalo_por_cliente = datetime.timedelta(seconds=intervalo_por_cliente) 
        
    #* Metodo para simular evento de la entrada de un cliente al sistema
    def llegada_cliente(self):
        self.hora_actual            = self.hora_llegada_cliente
        if self.ps == 0:
            self.ps                 = 1
            self.hora_fin_servicio  =  self.hora_llegada_cliente + self.duracion_servicio
        else:
            self.cola              += 1
        
        self.hora_llegada_cliente  += self.intervalo_por_cliente

    #* Metddo para simular evento de la salida de un cliente al sistema
    def fin_de_servicio(self):
        self.hora_actual            = self.hora_fin_servicio
        self.ps = 0
        if(self.cola > 0):
            self.ps                 = 1
            self.cola              -= 1
            self.hora_fin_servicio += self.duracion_servicio
        else:
            self.hora_fin_servicio  = None
    
    #* Metodo para elegir el evento que se va a simular
    def elegirEvento(self):
        for i in range(0,self.iteraciones):
            
            #? Segundos con numeros aleatorios
            #? Tiempo de llegada minimo  = 40sec
            #? Tiempo de llegada maximo  = 60sec
            #? Tiempo de servicio minimo = 30sec
            #? Tiempo de servicio minimo = 50sec
            self.duracion_servicio     = datetime.timedelta(seconds=random.randint(self.duracion_servicio_min, self.duracion_servicio_max))
            self.intervalo_por_cliente = datetime.timedelta(seconds=random.randint(self.intervalo_cliente_min, self.intervalo_cliente_max))
            
            if self.hora_fin_servicio == None:
                self.data.append([self.hora_actual.time(),
                      self.hora_llegada_cliente.time(),
                      '--------',
                      self.cola,
                      self.ps,
                      self.duracion_servicio.seconds,
                      self.intervalo_por_cliente.seconds])
            else:
                self.data.append([self.hora_actual.time(),
                      self.hora_llegada_cliente.time(),
                      self.hora_fin_servicio.time(),
                      self.cola,
                      self.ps,
                      self.duracion_servicio.seconds,
                      self.intervalo_por_cliente.seconds])
         
                         
            if(self.hora_fin_servicio == None or self.hora_llegada_cliente <= self.hora_fin_servicio):
                self.llegada_cliente()
            else:
                self.fin_de_servicio()
                
        return self.data


