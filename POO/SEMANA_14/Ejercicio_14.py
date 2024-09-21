

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Creamos una clase para armar nuestra agenda

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda privada de Estefi Toala")  # Título de la interfaz
        self.root.geometry("600x600")  # Ancho y largo de la interfaz
        self.root.config(bg="green yellow")  # Color de fondo de la interfaz gráfica

        # Creamos nuestra interfaz gráfica
        frame_entrada = tk.Frame(self.root)
        frame_entrada.pack(padx=5, pady=5)

        # Agregamos etiquetas para Fecha
        tk.Label(frame_entrada, text="Fecha").grid(row=0, column=0, padx=10, pady=10)
        self.date_entry = DateEntry(frame_entrada, width=10, background="darkblue", foreground="white", borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=10, pady=10)

        # Agregamos etiquetas para Hora
        tk.Label(frame_entrada, text="Hora: ").grid(row=1, column=0, padx=10, pady=10)
        self.time_entry = tk.Entry(frame_entrada)
        self.time_entry.grid(row=1, column=1, padx=10, pady=10)

        # Agregamos etiquetas para Descripción
        tk.Label(frame_entrada, text="Descripción: ").grid(row=2, column=0, padx=10, pady=10)
        self.desc_entry = tk.Entry(frame_entrada)
        self.desc_entry.grid(row=2, column=1, padx=10, pady=10)

        # Frame para los botones de control
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(padx=10, pady=10)

        # Botón para agregar evento
        tk.Button(frame_botones, text="Agregar", command=self.agregar_evento).pack(side=tk.LEFT, padx=10, pady=10)

        # Botón para eliminar evento
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_evento).pack(side=tk.LEFT, padx=10, pady=10)

        # Botón para salir de la aplicación
        tk.Button(frame_botones, text="Salir", command=self.root.quit).pack(side=tk.LEFT, padx=10, pady=10)

        # Frame para la lista de eventos
        frame_lista = tk.Frame(self.root)
        frame_lista.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Lista de eventos con Treeview
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")

        # Configuración de las columnas
        self.tree.column("Fecha", anchor="center", width=100)
        self.tree.column("Hora", anchor="center", width=100)
        self.tree.column("Descripción", anchor="center", width=200)

        # Encabezados de las columnas
        self.tree.heading("Fecha", text="Fecha", anchor="center")
        self.tree.heading("Hora", text="Hora", anchor="center")
        self.tree.heading("Descripción", text="Descripción", anchor="center")

        # Empaquetar Treeview
        self.tree.pack(fill=tk.BOTH, expand=True)

    # Método para agregar evento
    def agregar_evento(self):
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Alerta del sistema", "Rellena los campos")
            return

        # Insertar en la tabla
        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar campos de entrada
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    # Método para eliminar evento
    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if seleccion:
            confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el dato?")
            if confirmar:
                self.tree.delete(seleccion)
        else:
            messagebox.showwarning("Mensaje de alerta", "Selecciona un dato para eliminar")


# Crear la ventana principal
root = tk.Tk()

# Inicializar la clase de la agenda
app = AgendaApp(root)

# Ejecutar la aplicación
root.mainloop()
