import tkinter as tk
from tkinter import messagebox
from airline import LoadAirline, SaveAirline, PlotFlights


class AirlineInterface:
    def __init__(self, window):
        self.window = window
        self.window.title("Gestión de Aerolíneas - Paso 9")
        self.window.geometry("600x500")

        # Cargar los datos de la aerolínea desde los archivos de texto
        self.airline = LoadAirline("Vueling", "Aircrafts.txt", "operations.txt")

        # 1. Título principal
        self.title_label = tk.Label(window, text="Aerolínea: " + self.airline.name, font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # 2. Marco para poner los botones en fila
        self.button_frame = tk.Frame(window)
        self.button_frame.pack(pady=5)

        # Botón para mostrar los datos en texto
        self.btn_show = tk.Button(self.button_frame, text="Cargar Datos", command=self.show_all_data)
        self.btn_show.pack(side="left", padx=5)

        # Botón para abrir el gráfico de Matplotlib
        self.btn_plot = tk.Button(self.button_frame, text="Mostrar Gráfica", command=self.show_plot)
        self.btn_plot.pack(side="left", padx=5)

        # Botón para guardar los cambios en los ficheros
        self.btn_save = tk.Button(self.button_frame, text="Guardar Datos", command=self.save_data)
        self.btn_save.pack(side="left", padx=5)

        # 3. Caja de texto simple para mostrar la información
        self.text_info = tk.Text(window, width=70, height=20)
        self.text_info.pack(padx=10, pady=10)

        # Cargar los datos automáticamente en la pantalla al iniciar
        self.show_all_data()

    def show_all_data(self):
        # Limpiar la caja de texto
        self.text_info.delete("1.0", tk.END)

        # Imprimir la sección de Flota
        self.text_info.insert(tk.END, "--- FLEET ---\n")
        for aircraft in self.airline.fleet:
            info = f"Callsign: {aircraft.callsign} | Type: {aircraft.type} | Capacity: {aircraft.capacity}\n"
            self.text_info.insert(tk.END, info)

        # Imprimir la sección de Operaciones / Vuelos
        self.text_info.insert(tk.END, "\n--- OPERATIONS ---\n")
        for flight in self.airline.operations:
            info = f"ID: {flight.id} | Dep: {flight.departure_airport} ({flight.departure_time}) -> Arr: {flight.arrival_airport} ({flight.arrival_time}) | Pass: {flight.passengers}\n"
            self.text_info.insert(tk.END, info)

    def show_plot(self):
        # Llama a tu función PlotFlights de airline.py, que abre la ventana estándar de matplotlib
        PlotFlights(self.airline)

    def save_data(self):
        SaveAirline(self.airline, "Aircrafts.txt", "operations.txt")
        messagebox.showinfo("Guardado", "Datos guardados correctamente en los ficheros.")


# Punto de entrada de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AirlineInterface(root)
    root.mainloop()
