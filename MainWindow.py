import tkinter as tk
from tkinter import ttk
from Main import Sistema

class Window:
    def __init__(self):
         #CREACION VENTANA
        self.root = tk.Tk()
        self.root.resizable(tk.FALSE, tk.FALSE)
        
        self.lblTitulo = ttk.Label(self.root, text='Sistema', font=('Arial', 14, 'bold'))
        self.lblTitulo.grid(row=0, column=0, columnspan=5, pady=8)
        
        #Estilo tabla
        estilo = ttk.Style()
        estilo.theme_use("default")
        estilo.configure("Treeview",
                         background      = "white",
                         foreground      = "black",
                         rowheight       = 25,
                         fieldbackground ="white")
        estilo.map('Treeview',
                   background=[('selected', 'blue')])
        #CREACION TABLA
        self.tabla_simulacion = ttk.Treeview(self.root, selectmode = 'browse', height=12)
        self.tabla_simulacion.grid(
            row        = 1, 
            column     = 0, 
            sticky     = "nsew", 
            padx       = 5, 
            pady       = 10,
            columnspan = 4
        )

        self.tabla_simulacion.tag_configure('evenrow', background='white')
        self.tabla_simulacion.tag_configure('oddrow',  background='lightblue')
        
        #BARRASCROLL
        self.scrollbarTabla = ttk.Scrollbar(self.root, orient = "vertical", command=self.tabla_simulacion.yview)
        self.scrollbarTabla.grid(
            row    = 1, 
            column = 4, 
            sticky = "nsew",
            pady=10)

        #CONFIG TABLA
        self.tabla_simulacion.configure(xscrollcommand=self.scrollbarTabla.set)

        #NUMERO DE COLUMNAS
        self.tabla_simulacion["columns"] = ("iteracion", 
                                            "horaActual", 
                                            "horaProxCliente", 
                                            "horaFinServicio", 
                                            "horaComienzoDescanso", 
                                            "horaVueltaTrabajo",
                                            "Q", 
                                            "PS", 
                                            "S",
                                            "intervaloLlegadaCliente", 
                                            "duracionServicio"
                                            )

        #DEFINIENDO HEADING
        self.tabla_simulacion['show'] = 'headings'

        #AGREGAR COLUMNAS
        self.tabla_simulacion.column("iteracion",                width=50,  anchor='center')
        self.tabla_simulacion.column("horaActual",               width=130, anchor='center')
        self.tabla_simulacion.column("horaProxCliente",          width=130, anchor='center')
        self.tabla_simulacion.column("horaFinServicio",          width=130, anchor='center')
        self.tabla_simulacion.column("Q",                        width=50,  anchor='center')
        self.tabla_simulacion.column("PS",                       width=50,  anchor='center')
        self.tabla_simulacion.column("duracionServicio",         width=130, anchor='center')
        self.tabla_simulacion.column("intervaloLlegadaCliente",  width=130, anchor='center')
        self.tabla_simulacion.column("horaComienzoDescanso",     width=130, anchor='center')
        self.tabla_simulacion.column("horaVueltaTrabajo",        width=130, anchor='center')
        self.tabla_simulacion.column("S",                        width=50,  anchor='center')

        #HEADINGS COLUMNAS
        self.tabla_simulacion.heading("iteracion",               text="N°")
        self.tabla_simulacion.heading("horaActual",              text="Hs Actual")
        self.tabla_simulacion.heading("horaProxCliente",         text="Hs llegada prox cliente")
        self.tabla_simulacion.heading("horaFinServicio",         text="Hs fin de servicio")
        self.tabla_simulacion.heading("Q",                       text="Q")
        self.tabla_simulacion.heading("PS",                      text="PS")
        self.tabla_simulacion.heading("duracionServicio",        text="Duración Servicio")
        self.tabla_simulacion.heading("intervaloLlegadaCliente", text="Tiempo llegada")
        self.tabla_simulacion.heading("horaComienzoDescanso",    text="Hs comienzo descsanso")
        self.tabla_simulacion.heading("horaVueltaTrabajo",       text="Hs Vuelta Trabajo")
        self.tabla_simulacion.heading("S",                       text="S")

        self.lblCola                            = ttk.Label(self.root, text='Valor de cola inicial:', font=('Arial', 10))
        self.lblCola.grid(row=2, column=0, sticky="ens", pady=8)
        self.entryCola                          = tk.Entry(self.root)
        self.entryCola.grid(row=2, column=1, sticky="ens", pady=8)
        
        self.lblPs                              = ttk.Label(self.root, text='Valor de PS inicial:', font=('Arial', 10))
        self.lblPs.grid(row=2, column=2, sticky="ens", pady=8)
        self.entryPS                            = tk.Entry(self.root)
        self.entryPS.grid(row=2, column=3, sticky="ens", pady=8)
        
        self.lblDuracionServicio                = ttk.Label(self.root, text='Duracion del servicio minimo/maximo (segundos):', font=('Arial', 10))
        self.lblDuracionServicio.grid(row=3, column=0, sticky="ens", pady=8)
        self.entryDuracionServicio_minimo       = tk.Entry(self.root, width=8)
        self.entryDuracionServicio_minimo.grid(row=3, column=1, sticky="ns", pady=8)
        self.entryDuracionServicio_maximo       = tk.Entry(self.root, width=8)
        self.entryDuracionServicio_maximo.grid(row=3, column=1, sticky="ens", pady=8)
        
        self.lblIntervaloCliente                = ttk.Label(self.root, text='Tiempo llegada cliente minimo/maximo (segundos):', font=('Arial', 10))
        self.lblIntervaloCliente.grid(row=3, column=2, sticky="ens", pady=8)
        self.entryIntervaloCliente_minimo       = tk.Entry(self.root, width=8)
        self.entryIntervaloCliente_minimo.grid(row=3, column=3, sticky="ns", pady=8)
        self.entryIntervaloCliente_maximo              = tk.Entry(self.root, width=8)
        self.entryIntervaloCliente_maximo.grid(row=3, column=3, sticky="ens", pady=8)
        
        self.lblHoraActualInicial               = ttk.Label(self.root, text='Hora actual inicial (h:m:s):', font=('Arial', 10))
        self.lblHoraActualInicial.grid(row=4, column=0, sticky="ens", pady=8)
        self.entryHoraActualInicial             = tk.Entry(self.root)
        self.entryHoraActualInicial.grid(row=4, column=1, sticky="ens", pady=8)
        
        self.lblHoraLlegadaProxClienteInicial   = ttk.Label(self.root, text='Hora llegada prox cliente inicial (h:m:s):', font=('Arial', 10))
        self.lblHoraLlegadaProxClienteInicial.grid(row=4, column=2, sticky="ens", pady=8)
        self.entryHoraLlegadaProxClienteInicial = tk.Entry(self.root)
        self.entryHoraLlegadaProxClienteInicial.grid(row=4, column=3, sticky="ens", pady=8)
        
        self.lblHoraFinServicioInicial          = ttk.Label(self.root, text='Hora fin servicio inicial (h:m:s):', font=('Arial', 10))
        self.lblHoraFinServicioInicial.grid(row=5, column=0, sticky="ens", pady=8)
        self.entryHoraFinServicioInicial        = tk.Entry(self.root)
        self.entryHoraFinServicioInicial.grid(row=5, column=1, sticky="ens", pady=8)
        
        self.lblIteraciones                     = ttk.Label(self.root, text='Cantidad de iteraciones:', font=('Arial', 10))
        self.lblIteraciones.grid(row=5, column=2, sticky="ens", pady=8)
        self.entryIteraciones                   = tk.Entry(self.root)
        self.entryIteraciones.grid(row=5, column=3, sticky="ens", pady=8)
        
        self.lbl_duracion_descanso                = ttk.Label(self.root, text='Duracion descanso minimo/maximo (segundos):', font=('Arial', 10))
        self.lbl_duracion_descanso.grid(row=6, column=0, sticky="ens", pady=8)
        self.entry_intervalo_duracion_descanso_minimo       = tk.Entry(self.root, width=8)
        self.entry_intervalo_duracion_descanso_minimo.grid(row=6, column=1, sticky="ns", pady=8)
        self.entry_intervalo_duracion_descanso_maximo              = tk.Entry(self.root, width=8)
        self.entry_intervalo_duracion_descanso_maximo.grid(row=6, column=1, sticky="ens", pady=8)
        
        self.lbl_duracion_trabajo                = ttk.Label(self.root, text='Duracion trabajo minimo/maximo (segundos):', font=('Arial', 10))
        self.lbl_duracion_trabajo.grid(row=6, column=2, sticky="ens", pady=8)
        self.entry_intervalo_duracion_trabajo_minimo       = tk.Entry(self.root, width=8)
        self.entry_intervalo_duracion_trabajo_minimo.grid(row=6, column=3, sticky="ns", pady=8)
        self.entry_intervalo_duracion_trabajo_maximo              = tk.Entry(self.root, width=8)
        self.entry_intervalo_duracion_trabajo_maximo.grid(row=6, column=3, sticky="ens", pady=8)
        
        self.lbl_s                    = ttk.Label(self.root, text='S:', font=('Arial', 10))
        self.lbl_s.grid(row=7, column=0, sticky="ens", pady=8)
        self.entry_s                   = tk.Entry(self.root)
        self.entry_s.grid(row=7, column=1, sticky="ens", pady=8)
        
        self.lbl_hora_comienzo_descanso_inicial          = ttk.Label(self.root, text='Hora comienzo descanso inicial (h:m:s):', font=('Arial', 10))
        self.lbl_hora_comienzo_descanso_inicial.grid(row=7, column=2, sticky="ens", pady=8)
        self.entry_hora_comienzo_descanso_inicial        = tk.Entry(self.root)
        self.entry_hora_comienzo_descanso_inicial.grid(row=7, column=3, sticky="ens", pady=8)
        
        self.lbl_hora_vuelta_trabajo_inicial          = ttk.Label(self.root, text='Hora vuelta al trabajo inicial (h:m:s):', font=('Arial', 10))
        self.lbl_hora_vuelta_trabajo_inicial.grid(row=8, column=0, sticky="ens", pady=8)
        self.entry_hora_vuelta_trabajo_inicial        = tk.Entry(self.root)
        self.entry_hora_vuelta_trabajo_inicial.grid(row=8, column=1, sticky="ens", pady=8)
        
        #Boton para iniciar simulacion y llenar la tabla
        self.btnIniciar = tk.Button(self.root, text="Iniciar simulación", command=self.llenartabla_simulacion)
        self.btnIniciar.grid(
            row    = 8, 
            column = 3, 
            sticky = "nse",
            pady=8)

        self.root.tk.mainloop()

    def llenartabla_simulacion(self):
        self.tabla_simulacion.delete(*self.tabla_simulacion.get_children())
        
        hora_fin_servicio_aux = ("------" if self.entryHoraFinServicioInicial.get() == "" else self.entryHoraFinServicioInicial.get().split(sep=":"))
        
        
        sistema    = Sistema(
            int(self.entryCola.get()), 
            int(self.entryPS.get()), 
            self.entryHoraActualInicial.get().split(sep=":"),
            self.entryHoraLlegadaProxClienteInicial.get().split(sep=":"),
            self.entryHoraFinServicioInicial.get().split(sep=":"),
            int(self.entryIteraciones.get()),
            int(self.entryDuracionServicio_minimo.get()),
            int(self.entryDuracionServicio_maximo.get()),
            int(self.entryIntervaloCliente_minimo.get()),
            int(self.entryIntervaloCliente_maximo.get()),
            self.entry_hora_comienzo_descanso_inicial.get().split(sep=":"),
            self.entry_hora_vuelta_trabajo_inicial.get().split(sep=":"),
            int(self.entry_s.get()),
            int(self.entry_intervalo_duracion_descanso_minimo.get()),
            int(self.entry_intervalo_duracion_descanso_maximo.get()),
            int(self.entry_intervalo_duracion_trabajo_minimo.get()),
            int(self.entry_intervalo_duracion_trabajo_maximo.get()),
        )
        
        datosTabla = sistema.elegirEvento()
        for indice,dato in reversed(list(enumerate(datosTabla))):
            if indice % 2 == 0:
                self.tabla_simulacion.insert("",
                                        0,
                                        values=(
                                            indice,
                                            dato[0],
                                            dato[1],
                                            dato[2],
                                            dato[7],
                                            dato[8],
                                            dato[3],
                                            dato[4],
                                            dato[9],
                                            dato[5],
                                            dato[6]
                                        ),
                                        tags=('evenrow',)
                )
            else:
                self.tabla_simulacion.insert("",
                                        0,
                                        values=(
                                            indice,
                                            dato[0],
                                            dato[1],
                                            dato[2],
                                            dato[7],
                                            dato[8],
                                            dato[3],
                                            dato[4],
                                            dato[9],
                                            dato[5],
                                            dato[6]
                                        ),
                                        tags=('oddrow',)
                )

ventana = Window()