import datetime
import random
import pandas as pd
class Tabla():
    
    #* Inicializacion de variables
    def __init__(self) -> None:
        self.cola_a                  = int(input("Ingrese Valor de Qa inicial:"))
        self.cola_b                  = int(input("Ingrese Valor de Qb inicial:"))
        self.ps                      = int(input("Ingrese Valor de PS inicial:"))
        self.data                    = []
        hora_actual_input            = (input("Ingrese hora actual inicial (h:m:s):")).split(sep=":") #9:0:32
        hora_llegada_cliente_a_input = (input("Ingrese hora llegda cliente A inicial (h:m:s):")).split(sep=":") #9:0:49
        hora_llegada_cliente_b_input = (input("Ingrese hora llegda cliente B inicial (h:m:s):")).split(sep=":") #9:0:49
        hora_fin_serivicio_input     = (input("Ingrese hora fin servicio inicial (h:m:s):")).split(sep=":") #9:01:07
        
        self.hora_actual               = datetime.datetime(year   = datetime.date.today().year, 
                                                           month  = datetime.date.today().month, 
                                                           day    = datetime.date.today().day, 
                                                           hour   = int(hora_actual_input[0]), 
                                                           minute = int(hora_actual_input[1]), 
                                                           second = int(hora_actual_input[2]))
         
        self.hora_llegada_cliente_a      = datetime.datetime(year   = datetime.date.today().year, 
                                                           month  = datetime.date.today().month, 
                                                           day    = datetime.date.today().day, 
                                                           hour   = int(hora_llegada_cliente_a_input[0]), 
                                                           minute = int(hora_llegada_cliente_a_input[1]), 
                                                           second = int(hora_llegada_cliente_a_input[2]))
        
        self.hora_llegada_cliente_b      = datetime.datetime(year   = datetime.date.today().year, 
                                                           month  = datetime.date.today().month, 
                                                           day    = datetime.date.today().day, 
                                                           hour   = int(hora_llegada_cliente_b_input[0]), 
                                                           minute = int(hora_llegada_cliente_b_input[1]), 
                                                           second = int(hora_llegada_cliente_b_input[2]))
         
        self.hora_fin_servicio         = datetime.datetime(year   = datetime.date.today().year, 
                                                           month  = datetime.date.today().month, 
                                                           day    = datetime.date.today().day, 
                                                           hour   = int(hora_fin_serivicio_input[0]), 
                                                           minute = int(hora_fin_serivicio_input[1]), 
                                                           second = int(hora_fin_serivicio_input[2]))
        
        self.tiempo_de_llegada_cliente_a_minimo  = int(input("Ingrese valor minimo de tiempo de llegada del cliente A(minutos):"))#10 #tiempo en segundos
        self.tiempo_de_llegada_cliente_a_maximo  = int(input("Ingrese valor maximo de tiempo de llegada del cliente A(minutos):"))#10 #tiempo en segundos
        self.tiempo_de_llegada_cliente_b_minimo  = int(input("Ingrese valor minimo de tiempo de llegada del cliente B(minutos):"))#10 #tiempo en segundos
        self.tiempo_de_llegada_cliente_b_maximo  = int(input("Ingrese valor maximo de tiempo de llegada del cliente B(minutos):"))#10 #tiempo en segundos
        self.tiempo_de_servicio_minimo           = int(input("Ingrese valor minimo de duracion del servicio (segundos):"))#50 #tiempo en segundos
        self.tiempo_de_servicio_maximo           = int(input("Ingrese valor maximo de duracion del servicio (segundos):"))#50 #tiempo en segundos
        
        self.data                                = []
        #Variables Auxiliares
        self.flag_fin_servicio                   = False

        
    #* Metodo para simular evento de la entrada de un cliente al sistema
    def llegada_cliente_a(self):
        self.hora_actual            = self.hora_llegada_cliente_a
        if self.ps == 0:
            self.ps                 = 1
            self.hora_fin_servicio  =  self.hora_llegada_cliente_a + self.duracion_servicio
        else:
            self.cola_a            += 1
        
        self.hora_llegada_cliente_a  += self.intervalo_por_cliente_a
        
         #* Metodo para simular evento de la entrada de un cliente al sistema
    def llegada_cliente_b(self):
        self.hora_actual            = self.hora_llegada_cliente_b
        if self.ps == 0:
            if self.cola_a > 0:
                self.cola_b += 1
            else:
                self.ps                 = 1
                self.hora_fin_servicio  =  self.hora_llegada_cliente_b + self.duracion_servicio
        else:
            self.cola_b            += 1
        
        self.hora_llegada_cliente_b  += self.intervalo_por_cliente_b

    #* Metddo para simular evento de la salida de un cliente al sistema
    def fin_de_servicio(self):
        self.hora_actual            = self.hora_fin_servicio
        self.ps = 0
        if(self.cola_a > 0):
            self.ps                 = 1
            self.cola_a            -= 1
            self.hora_fin_servicio  = self.hora_actual + self.duracion_servicio
        else:
            if self.cola_b > 0:
                self.cola_b -= 1
                self.ps      = 1
                self.hora_fin_servicio = self.hora_actual + self.duracion_servicio
            else:
                self.hora_fin_servicio += datetime.timedelta(hours=10)
                self.flag_fin_servicio  = True
    
    #* Metodo para elegir el evento que se va a simular
    def elegirEvento(self):
        for i in range(0,20):
            
            self.duracion_servicio       = datetime.timedelta(seconds=random.randint(self.tiempo_de_servicio_minimo,self.tiempo_de_servicio_maximo))
            self.intervalo_por_cliente_a = datetime.timedelta(minutes=random.randint(self.tiempo_de_llegada_cliente_a_minimo, self.tiempo_de_llegada_cliente_a_maximo))
            self.intervalo_por_cliente_b = datetime.timedelta(minutes=random.randint(self.tiempo_de_llegada_cliente_b_minimo, self.tiempo_de_llegada_cliente_b_maximo))
            
            hora_fin_servicio_aux = ('--------' if self.flag_fin_servicio else self.hora_fin_servicio.time())
            
            self.data.append([self.hora_actual.time(),
                      self.hora_llegada_cliente_a.time(),
                      self.hora_llegada_cliente_b.time(),
                      hora_fin_servicio_aux,
                      self.cola_a,
                      self.cola_b,
                      self.ps,
                      self.duracion_servicio.seconds,
                      ])
         
            if(self.hora_llegada_cliente_a <= self.hora_llegada_cliente_b and self.hora_llegada_cliente_a <= self.hora_fin_servicio):
                self.llegada_cliente_a()
            elif(self.hora_llegada_cliente_b <= self.hora_fin_servicio):
                self.llegada_cliente_b()
            else:
                self.fin_de_servicio()
                
        print(pd.DataFrame(data=self.data, columns=['|Hora Actual', '|Hora prox cliente A', '|Hora prox cliente B', '|Hora fin serv', '|Qa', '|Qb', '|PS', '|Tiempo serv']))


sistema = Tabla()
sistema.elegirEvento()

