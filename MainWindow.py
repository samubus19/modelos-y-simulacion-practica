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
        self.tablaSimulacion = ttk.Treeview(self.root, selectmode = 'browse', height=12)
        self.tablaSimulacion.grid(
            row        = 1, 
            column     = 0, 
            sticky     = "nsew", 
            padx       = 5, 
            pady       = 10,
            columnspan = 4
        )

        self.tablaSimulacion.tag_configure('evenrow', background='white')
        self.tablaSimulacion.tag_configure('oddrow',  background='lightblue')
        
        #BARRASCROLL
        self.scrollbarTabla = ttk.Scrollbar(self.root, orient = "vertical", command=self.tablaSimulacion.yview)
        self.scrollbarTabla.grid(
            row    = 1, 
            column = 4, 
            sticky = "nsew",
            pady=10)

        #CONFIG TABLA
        self.tablaSimulacion.configure(xscrollcommand=self.scrollbarTabla.set)

        #NUMERO DE COLUMNAS
        self.tablaSimulacion["columns"] = ("iteracion", "horaActual", "horaProxCliente", "horaFinServicio", "Q", "PS", "duracionServicio", "intervaloLlegadaCliente")

        #DEFINIENDO HEADING
        self.tablaSimulacion['show'] = 'headings'

        #AGREGAR COLUMNAS
        self.tablaSimulacion.column("iteracion",                width=50,  anchor='center')
        self.tablaSimulacion.column("horaActual",               width=150, anchor='center')
        self.tablaSimulacion.column("horaProxCliente",          width=150, anchor='center')
        self.tablaSimulacion.column("horaFinServicio",          width=150, anchor='center')
        self.tablaSimulacion.column("Q",                        width=150, anchor='center')
        self.tablaSimulacion.column("PS",                       width=150, anchor='center')
        self.tablaSimulacion.column("duracionServicio",         width=150, anchor='center')
        self.tablaSimulacion.column("intervaloLlegadaCliente",  width=150, anchor='center')

        #HEADINGS COLUMNAS
        self.tablaSimulacion.heading("iteracion",               text="N°")
        self.tablaSimulacion.heading("horaActual",              text="Hora Actual")
        self.tablaSimulacion.heading("horaProxCliente",         text="Hora llegada prox cliente")
        self.tablaSimulacion.heading("horaFinServicio",         text="Hora fin de servicio")
        self.tablaSimulacion.heading("Q",                       text="Q")
        self.tablaSimulacion.heading("PS",                      text="PS")
        self.tablaSimulacion.heading("duracionServicio",        text="Duración Servicio")
        self.tablaSimulacion.heading("intervaloLlegadaCliente", text="Tiempo llegada")

        self.lblCola                            = ttk.Label(self.root, text='Valor de cola inicial:', font=('Arial', 10))
        self.lblCola.grid(row=2, column=0, sticky="ens", pady=8)
        self.entryCola                          = tk.Entry(self.root)
        self.entryCola.grid(row=2, column=1, sticky="ens", pady=8)
        
        self.lblPs                              = ttk.Label(self.root, text='Valor de PS inicial:', font=('Arial', 10))
        self.lblPs.grid(row=2, column=2, sticky="ens", pady=8)
        self.entryPS                            = tk.Entry(self.root)
        self.entryPS.grid(row=2, column=3, sticky="ens", pady=8)
        
        self.lblDuracionServicio                = ttk.Label(self.root, text='Duracion del servicio (segundos):', font=('Arial', 10))
        self.lblDuracionServicio.grid(row=3, column=0, sticky="ens", pady=8)
        self.entryDuracionServicio              = tk.Entry(self.root)
        self.entryDuracionServicio.grid(row=3, column=1, sticky="ens", pady=8)
        
        self.lblIntervaloCliente                = ttk.Label(self.root, text='Tiempo llegada cliente (segundos):', font=('Arial', 10))
        self.lblIntervaloCliente.grid(row=3, column=2, sticky="ens", pady=8)
        self.entryIntervaloCliente              = tk.Entry(self.root)
        self.entryIntervaloCliente.grid(row=3, column=3, sticky="ens", pady=8)
        
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
        
        #Boton para iniciar simulacion y llenar la tabla
        self.btnIniciar = tk.Button(self.root, text="Iniciar simulación", command=self.llenarTablaSimulacion)
        self.btnIniciar.grid(
            row    = 6, 
            column = 3, 
            sticky = "nse",
            pady=8)
        #!LLeno la tabla de productos
        # self.llenarTablaSimulacion()

        self.root.tk.mainloop()

    def llenarTablaSimulacion(self):
        sistema    = Sistema(
            int(self.entryCola.get()), 
            int(self.entryPS.get()), 
            int(self.entryDuracionServicio.get()), 
            int(self.entryIntervaloCliente.get()), 
            self.entryHoraActualInicial.get().split(sep=":"),
            self.entryHoraLlegadaProxClienteInicial.get().split(sep=":"),
            self.entryHoraFinServicioInicial.get().split(sep=":"),
            int(self.entryIteraciones.get())
        )

        datosTabla = sistema.elegirEvento()
        for indice,dato in reversed(list(enumerate(datosTabla))):
            if indice % 2 == 0:
                self.tablaSimulacion.insert("",
                                        0,
                                        values=(
                                            indice,
                                            dato[0],
                                            dato[1],
                                            dato[2],
                                            dato[3],
                                            dato[4],
                                            dato[5],
                                            dato[6]
                                        ),
                                        tags=('evenrow',)
                )
            else:
                self.tablaSimulacion.insert("",
                                        0,
                                        values=(
                                            indice,
                                            dato[0],
                                            dato[1],
                                            dato[2],
                                            dato[3],
                                            dato[4],
                                            dato[5],
                                            dato[6]
                                        ),
                                        tags=('oddrow',)
                )

ventana = Window()