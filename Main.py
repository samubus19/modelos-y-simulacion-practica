import datetime
import random
import pandas as pd
class Sistema():
    
    #* Inicializacion de variables
    def __init__(self, cola, ps, duracion_servicio, intervalo_por_cliente, hora_actual_inicial, hora_llegada_cliente_inicial, hora_fin_servicio_inicial, iteraciones):
        self.iteraciones           = iteraciones
        self.cola                  = cola
        self.ps                    = ps
        self.data                  = []
        self.hora_actual           = datetime.datetime(2022, 6, 22, int(hora_actual_inicial[0]), int(hora_actual_inicial[1]), int(hora_actual_inicial[2]))
        self.hora_llegada_cliente  = datetime.datetime(2022, 6, 22, int(hora_llegada_cliente_inicial[0]), int(hora_llegada_cliente_inicial[1]), int(hora_llegada_cliente_inicial[2]))
        self.hora_fin_servicio     = datetime.datetime(2022, 6, 22, int(hora_fin_servicio_inicial[0]), int(hora_fin_servicio_inicial[1]), int(hora_fin_servicio_inicial[2]))
        self.duracion_servicio     = datetime.timedelta(seconds=duracion_servicio)
        self.intervalo_por_cliente = datetime.timedelta(seconds=intervalo_por_cliente)
        
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
            #? le asgino un valor grande a hora de fin de servicio para que se ejecute el otro evento
            self.hora_fin_servicio  = datetime.datetime(2023, 6, 22, 23, 0, 0)
    
    #* Metodo para elegir el evento que se va a simular
    def elegirEvento(self):
        for i in range(0,self.iteraciones):
            
            #? Segundos con numeros aleatorios
            #? Tiempo de llegada minimo  = 40sec
            #? Tiempo de llegada maximo  = 60sec
            #? Tiempo de servicio minimo = 30sec
            #? Tiempo de servicio minimo = 50sec
            # self.duracion_servicio     = datetime.timedelta(seconds=random.randint(30,50))
            # self.intervalo_por_cliente = datetime.timedelta(seconds=random.randint(40,60))
            
            self.data.append([self.hora_actual.time(),
                      self.hora_llegada_cliente.time(),
                      self.hora_fin_servicio.time(),
                      self.cola,
                      self.ps,
                      self.duracion_servicio.seconds,
                      self.intervalo_por_cliente.seconds])
         
            # if(self.hora_fin_servicio.time() == self.hora_llegada_cliente.time()):
            #     #? Elijo cual evento ejecutar
            #     self.hora_actual        = self.hora_llegada_cliente
            #     self.llegada_cliente()
            #     # self.hora_actual        = self.hora_fin_servicio
            #     # self.fin_de_servicio()
                
            if(self.hora_llegada_cliente <= self.hora_fin_servicio):
                self.llegada_cliente()
            else:
                self.fin_de_servicio()
                
        return self.data


