import datetime
import random
import pandas as pd

# Eventos.
# 1) Llegada de un cliente al sistema
# 2) Fin del servicio.
# 3) Llegada del servidor (regreso al PS)
# 4) Salida del servidor (abandono del PS).
# Variables de estado.
# 1) Estado de ocupado (ps=1) o libre (ps=0) del puesto de servicio.
# 2) Cantidad de clientes en cola (q).
# 3) Presencia (S=1) o ausencia(S=0) del servidor.
class Sistema():
    
    #* Inicializacion de variables
    def __init__(self, 
                 cola, 
                 ps, 
                 hora_actual_inicial, 
                 hora_llegada_cliente_inicial, 
                 hora_fin_servicio_inicial, 
                 iteraciones, 
                 duracion_servicio_min, 
                 duracion_servicio_max, 
                 intervalo_cliente_min, 
                 intervalo_cliente_max,
                 hora_comienzo_descanso_inicial,
                 hora_vuelta_trabajo_inicial,
                 s,
                 duracion_descanso_min, 
                 duracion_descanso_max, 
                 duracion_trabajo_min, 
                 duracion_trabajo_max):
        self.s                               = s
        self.hora_comienzo_descanso          = datetime.datetime(year=2022, 
                                                                 month=6, 
                                                                 day=22,
                                                                 hour=int(hora_comienzo_descanso_inicial[0]),
                                                                 minute=int(hora_comienzo_descanso_inicial[1]),
                                                                 second=int(hora_comienzo_descanso_inicial[2]))
        self.hora_vuelta_trabajo             = datetime.datetime(year=2023, 
                                                                 month=6, 
                                                                 day=22,
                                                                 hour=int(hora_vuelta_trabajo_inicial[0]),
                                                                 minute=int(hora_vuelta_trabajo_inicial[1]),
                                                                 second=int(hora_vuelta_trabajo_inicial[2]))
        self.iteraciones                     = iteraciones
        self.cola                            = cola
        self.ps                              = ps
        self.hora_actual                     = datetime.datetime(year=2022, 
                                                                 month=6, 
                                                                 day=22, 
                                                                 hour=int(hora_actual_inicial[0]), 
                                                                 minute=int(hora_actual_inicial[1]), 
                                                                 second=int(hora_actual_inicial[2]))
        self.hora_llegada_cliente            = datetime.datetime(year=2022, 
                                                                 month=6, 
                                                                 day=22, 
                                                                 hour=int(hora_llegada_cliente_inicial[0]), 
                                                                 minute=int(hora_llegada_cliente_inicial[1]), 
                                                                 second=int(hora_llegada_cliente_inicial[2]))
        self.hora_fin_servicio               = datetime.datetime(year=2022, 
                                                                 month=6, 
                                                                 day=22, 
                                                                 hour=int(hora_fin_servicio_inicial[0]), 
                                                                 minute=int(hora_fin_servicio_inicial[1]), 
                                                                 second=int(hora_fin_servicio_inicial[2]))
        self.duracion_servicio_min           = duracion_servicio_min
        self.duracion_servicio_max           = duracion_servicio_max
        self.intervalo_cliente_min           = intervalo_cliente_min
        self.intervalo_cliente_max           = intervalo_cliente_max
        self.intervalo_duracion_trabajo_min  = duracion_trabajo_min
        self.intervalo_duracion_trabajo_max  = duracion_trabajo_max
        self.intervalo_duracion_descanso_min = duracion_descanso_min
        self.intervalo_duracion_descanso_max = duracion_descanso_max
        
        self.data                            = [] #Arreglo para guardar valores ingresados por teclado
        self.hs_comienzo_descanso_flag       = False
        self.hs_fin_servicio_flag            = False
        self.hs_vuelta_trabajo_flag          = False
        
    def salida_servidor(self):
        
        self.hora_actual               = self.hora_comienzo_descanso
        self.s                         = 0
        self.duracion_descanso         = datetime.timedelta(seconds=random.randint(self.intervalo_duracion_descanso_min, self.intervalo_duracion_descanso_max)) 
        self.hora_vuelta_trabajo       = self.hora_comienzo_descanso + self.duracion_descanso
        if self.ps != 0:
            self.hora_fin_servicio    += self.duracion_descanso
        self.hora_comienzo_descanso   += datetime.timedelta(hours=5)
        self.hs_comienzo_descanso_flag = True
        self.hs_vuelta_trabajo_flag    = False
        
    def regreso_del_servidor(self):
        self.hora_actual               = self.hora_vuelta_trabajo
        self.s                         = 1   
        self.duracion_trabajo       = datetime.timedelta(seconds=random.randint(self.intervalo_duracion_trabajo_min, self.intervalo_duracion_trabajo_max)) 
        self.hora_comienzo_descanso    = self.hora_actual + self.duracion_trabajo
        self.hora_vuelta_trabajo      += datetime.timedelta(hours=5)
        self.hs_vuelta_trabajo_flag    = True
        self.hs_comienzo_descanso_flag = False
        
        
    #* Metodo para simular evento de la entrada de un cliente al sistema
    def llegada_cliente(self):
        self.hora_actual                = self.hora_llegada_cliente
        if self.ps == 0:
            self.ps                     = 1
            if self.s == 0:
                self.hora_fin_servicio  =  self.hora_vuelta_trabajo + self.duracion_servicio
            else:
                self.hora_fin_servicio  = self.hora_llegada_cliente + self.duracion_servicio
            self.hs_fin_servicio_flag   = False
        else:
            self.cola                  += 1
        
        self.hora_llegada_cliente      += self.intervalo_por_cliente

    #* Metddo para simular evento de la salida de un cliente al sistema
    def fin_de_servicio(self):
        self.hora_actual              = self.hora_fin_servicio
        self.ps = 0
        if(self.cola > 0):
            self.ps                   = 1
            self.cola                -= 1
            self.hora_fin_servicio   += self.duracion_servicio
        else:
            self.hora_fin_servicio   += datetime.timedelta(hours=5)
            self.hs_fin_servicio_flag = True
    
    #* Metodo para elegir el evento que se va a simular
    def elegirEvento(self):
        for i in range(0,self.iteraciones):
            
            self.duracion_servicio      = datetime.timedelta(seconds=random.randint(self.duracion_servicio_min, self.duracion_servicio_max))
            self.intervalo_por_cliente  = datetime.timedelta(seconds=random.randint(self.intervalo_cliente_min, self.intervalo_cliente_max))
             
            hora_fin_servicio_aux       = ('--------' if self.hs_fin_servicio_flag else self.hora_fin_servicio.time())
            hora_comienzo_descanso_aux  = ('--------' if self.hs_comienzo_descanso_flag else self.hora_comienzo_descanso.time())
            hora_vuelta_trabajo_aux     = ('--------' if self.hs_vuelta_trabajo_flag else self.hora_vuelta_trabajo.time())
            
            self.data.append([self.hora_actual.time(),
                    self.hora_llegada_cliente.time(),
                    hora_fin_servicio_aux,
                    self.cola,
                    self.ps,
                    self.duracion_servicio.seconds,
                    self.intervalo_por_cliente.seconds,
                    hora_comienzo_descanso_aux,
                    hora_vuelta_trabajo_aux,
                    self.s])
            
                         
            if((self.hora_llegada_cliente <= self.hora_fin_servicio) and (self.hora_llegada_cliente <= self.hora_comienzo_descanso) and (self.hora_llegada_cliente <= self.hora_vuelta_trabajo)):
                self.llegada_cliente()
            elif ((self.hora_fin_servicio <= self.hora_comienzo_descanso) and (self.hora_fin_servicio <= self.hora_vuelta_trabajo)):
                self.fin_de_servicio()
            elif (self.hora_comienzo_descanso <= self.hora_vuelta_trabajo):
                self.salida_servidor()
            else :
                self.regreso_del_servidor()
                
                
        return self.data


