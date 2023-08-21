import tkinter as tk
from tkinter import messagebox
import datetime
import timeit
import psutil

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

class DateSortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ordenador de Fechas con Bubble Sort")

        self.dates = []

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=20, pady=20)

        self.date_entry = tk.Entry(self.input_frame, width=15)
        self.date_entry.pack(side=tk.LEFT)

        self.add_button = tk.Button(self.input_frame, text="Agregar Fecha", command=self.add_date)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.sort_button = tk.Button(self.root, text="Ordenar Fechas", command=self.sort_dates)
        self.sort_button.pack(pady=10)

        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(padx=20, pady=20)

        self.sorted_dates_label = tk.Label(self.result_frame, text="USO DEL METODO BUBBLE SORT",
                                           font=("Helvetica", 16, "bold"))
        self.sorted_dates_label.pack()

        self.sorted_dates_text = tk.Text(self.result_frame, height=10, width=40)
        self.sorted_dates_text.pack()

        self.time_label = tk.Label(self.result_frame, text="Tiempo de Ejecución:", font=("Helvetica", 12, "bold"))
        self.time_label.pack(pady=10)

        self.memory_label = tk.Label(self.result_frame, text="Uso de Memoria:", font=("Helvetica", 12, "bold"))
        self.memory_label.pack(pady=10)

    def add_date(self):
        date_str = self.date_entry.get()
        try:
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            self.dates.append(date_obj)
            self.date_entry.delete(0, tk.END)
            self.update_dates_text()
            messagebox.showinfo("Éxito", "Fecha agregada correctamente.")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto. Utilice el formato AAAA-MM-DD.")

    def sort_dates(self):
        if len(self.dates) > 0:
            setup_code = f"from __main__ import bubble_sort, psutil; dates = {self.dates}"
            stmt = "bubble_sort(dates.copy())"
            time = timeit.timeit(stmt, setup=setup_code, number=100, globals=globals())

            bubble_sort(self.dates.copy())
            sorted_dates_str = [date.strftime('%Y-%m-%d') for date in self.dates]
            self.sorted_dates_text.delete(1.0, tk.END)
            self.sorted_dates_text.insert(tk.END, '\n'.join(sorted_dates_str))

            memory_used = psutil.Process().memory_info().rss / (1024 * 1024)  # Obtener memoria en MB
            self.memory_label.config(text=f"Uso de Memoria: {memory_used:.2f} MB")

            self.time_label.config(text=f"Tiempo de Ejecución: {time:.4f} segundos")
        else:
            messagebox.showwarning("Advertencia", "No se han ingresado fechas para ordenar.")

    def update_dates_text(self):
        dates_str = [date.strftime('%Y-%m-%d') for date in self.dates]
        self.sorted_dates_text.delete(1.0, tk.END)
        self.sorted_dates_text.insert(tk.END, '\n'.join(dates_str))

if __name__ == "__main__":
    root = tk.Tk()
    app = DateSortingApp(root)
    root.mainloop()
