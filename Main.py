import datetime
import pandas as pd
class Tabla():
    
    #* Inicializacion de variables
    def __init__(self) -> None:
        self.z                     = int(input("Ingrese valor de z (zona de seguridad) inicial 1/0: "))
        self.cola                  = int(input("Ingrese valor de cola inicial: "))
        self.ps                    = (0 if self.z == 1  else int(input("Ingrese valor de ps: ")))
        self.data                  = []
        
        hora_actual_input          = input("Ingrese hora actual inicial (h:m:s): ").split(":")
        hora_llegada_cliente_input = input("Ingrese hora de llegada inicial (h:m:s): ").split(":")
        hora_fin_servicio_input    = input("Ingrese hora de fin de servicio inicial (h:m:s): ").split(":")
        hora_salida_z_input        = input("Ingrese hora de salidad de Z inicial (h:m:s): ").split(":")
        
        self.hora_actual           = datetime.datetime(year   = datetime.date.today().year, 
                                                       month  = datetime.date.today().month, 
                                                       day    = datetime.date.today().day, 
                                                       hour   = int(hora_actual_input[0]), 
                                                       minute = int(hora_actual_input[1]), 
                                                       second = int(hora_actual_input[2]))
        
        self.hora_llegada_cliente  = datetime.datetime(year   = datetime.date.today().year, 
                                                       month  = datetime.date.today().month, 
                                                       day    = datetime.date.today().day, 
                                                       hour   = int(hora_llegada_cliente_input[0]), 
                                                       minute = int(hora_llegada_cliente_input[1]), 
                                                       second = int(hora_llegada_cliente_input[2]))
        
        self.hora_salida_z         = datetime.datetime(year   = datetime.date.today().year, 
                                                       month  = datetime.date.today().month, 
                                                       day    = datetime.date.today().day, 
                                                       hour   = int(hora_salida_z_input[0]), 
                                                       minute = int(hora_salida_z_input[1]), 
                                                       second = int(hora_salida_z_input[2]))
        
        self.hora_fin_servicio     = datetime.datetime(year   = datetime.date.today().year, 
                                                       month  = datetime.date.today().month, 
                                                       day    = datetime.date.today().day, 
                                                       hour   = int(hora_fin_servicio_input[0]), 
                                                       minute = int(hora_fin_servicio_input[1]), 
                                                       second = int(hora_fin_servicio_input[2]))
        
        self.duracion_servicio     = datetime.timedelta(minutes=int(input("Ingrese duracion del servicio (minutos): ")))
        self.intervalo_por_cliente = datetime.timedelta(minutes=int(input("Ingrese tiempo de llegada de cliente (minutos): ")))
        self.duracion_en_zona      = datetime.timedelta(minutes=int(input("Ingrese tiempo de cliente en zona (minutos): ")))
        
        self.hora_fin_servicio_flag = True
        self.hora_salida_de_z_flag  = True
        
        
    #* Metodo para simular evento de la entrada de un cliente al sistema
    def llegada_cliente_al_sistema(self):
        self.hora_actual               = self.hora_llegada_cliente
        if self.ps == 0 and self.z == 0:
            self.z                     = 1
            self.hora_salida_z         = self.hora_actual + self.duracion_en_zona
            self.hora_salida_de_z_flag = True
        else:
            self.cola                 += 1
        self.hora_llegada_cliente     += self.intervalo_por_cliente

    #* Metddo para simular evento de la salida de un cliente al sistema
    def fin_de_servicio(self):
        self.hora_actual            = self.hora_fin_servicio
        self.ps                     = 0
        if(self.cola > 0):
            self.z                  = 1
            self.cola              -= 1
            self.hora_salida_z      = self.hora_actual + self.duracion_en_zona
            self.hora_salida_de_z_flag = True
        self.hora_fin_servicio += datetime.timedelta(hours=10)
        self.hora_fin_servicio_flag = False

    def salida_zona_seguridad(self):
        self.hora_actual = self.hora_salida_z
        self.z                  = 0
        self.ps                 = 1
        self.hora_fin_servicio  = self.hora_actual + self.duracion_servicio
        self.hora_fin_servicio_flag = True
        self.hora_salida_z     += datetime.timedelta(hours=10)
        self.hora_salida_de_z_flag = False
    
    #* Metodo para elegir el evento que se va a simular
    def elegirEvento(self):
        for i in range(0,25):
            
            hora_fin_servicio_aux = ('--------' if not self.hora_fin_servicio_flag  else self.hora_fin_servicio.time())
            hora_salida_z_aux     = ('--------' if not self.hora_salida_de_z_flag else self.hora_salida_z.time())
            
            self.data.append([
                      self.hora_actual.time(),
                      self.hora_llegada_cliente.time(),
                      hora_salida_z_aux,
                      hora_fin_servicio_aux,
                      self.cola,
                      self.ps,
                      self.z,
                      ])
       
            if((self.hora_llegada_cliente <= self.hora_fin_servicio) and (self.hora_llegada_cliente <= self.hora_salida_z)):
                self.llegada_cliente_al_sistema()
            elif(self.hora_salida_z <= self.hora_fin_servicio):
                self.salida_zona_seguridad()
            else:
                self.fin_de_servicio()
                
        print(pd.DataFrame(data=self.data, columns=['|Hora Actual', '|Hora prox cliente', '|Salida zona', '|Hora fin serv', '|Q', '|PS', '|Z']))


sistema = Tabla()
sistema.elegirEvento()

