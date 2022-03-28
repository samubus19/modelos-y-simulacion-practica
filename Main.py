import datetime
import random
import pandas as pd
class Tabla():
    
    #* Inicializacion de variables
    def __init__(self) -> None:
        self.cola                  = 3
        self.ps                    = 1
        self.data                  = []
        self.hora_actual           = datetime.datetime(2022, 6, 22, 8, 0, 0)
        self.hora_llegada_cliente  = datetime.datetime(2022, 6, 22, 8, 5, 0)
        self.hora_fin_servicio     = datetime.datetime(2022, 6, 22, 8, 3, 0)
        self.duracion_servicio     = datetime.timedelta(seconds=40)
        self.intervalo_por_cliente = datetime.timedelta(seconds=45)
        
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
            #? Preguntar que hacer con la hora de fin de servicio
            #? le asgino un valor grande a hora de fin de servicio para que se ejecute el otro evento
            self.hora_fin_servicio  = datetime.datetime(2023, 6, 22, 23, 0, 0)
    
    #* Metodo para elegir el evento que se va a simular
    def elegirEvento(self):
        for i in range(0,9):
            
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
                
        print(pd.DataFrame(data=self.data, columns=['|Hora Actual', '|Hora prox cliente', '|Hora fin serv', '|Q', '|PS', '|Tiempo serv', '|Llegada prox cliente']))


sistema = Tabla()
sistema.elegirEvento()

