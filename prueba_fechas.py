import tkinter as tk
from tkinter import messagebox
import datetime
import timeit


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


class DateSortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ordenador de Fechas con Quick Sort y Merge Sort")

        self.dates = []

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=20, pady=20)

        self.date_entry = tk.Entry(self.input_frame, width=15)
        self.date_entry.pack(side=tk.LEFT)

        self.add_button = tk.Button(self.input_frame, text="Agregar Fecha", command=self.add_date)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.quick_sort_button = tk.Button(self.root, text="Ordenar Fechas (Quick Sort)", command=self.sort_dates_quick)
        self.quick_sort_button.pack(pady=10)

        self.merge_sort_button = tk.Button(self.root, text="Ordenar Fechas (Merge Sort)", command=self.sort_dates_merge)
        self.merge_sort_button.pack(pady=10)

        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(padx=20, pady=20)

        self.sorted_dates_label = tk.Label(self.result_frame, text="Fechas Ordenadas:", font=("Helvetica", 16, "bold"))
        self.sorted_dates_label.pack()

        self.sorted_dates_text = tk.Text(self.result_frame, height=10, width=40)
        self.sorted_dates_text.pack()

        self.time_label = tk.Label(self.result_frame, text="Tiempo de Ejecución:", font=("Helvetica", 12, "bold"))
        self.time_label.pack(pady=10)

    def add_date(self):
        date_str = self.date_entry.get()
        try:
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            self.dates.append(date_obj)
            self.date_entry.delete(0, tk.END)
            self.update_dates_text()
            messagebox.showinfo("Éxito", "Fecha agregada correctamente.")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto. Utilice el formato YYYY-MM-DD.")

    def sort_dates_quick(self):
        if len(self.dates) > 0:
            setup_code = f"from __main__ import quick_sort; dates = {self.dates}"
            stmt = "sorted_dates = quick_sort(dates.copy())"
            time = timeit.timeit(stmt, setup=setup_code, number=100, globals=globals())

            sorted_dates = quick_sort(self.dates.copy())
            if sorted_dates is not None:
                sorted_dates_str = [date.strftime('%Y-%m-%d') for date in sorted_dates]
                self.sorted_dates_text.delete(1.0, tk.END)
                self.sorted_dates_text.insert(tk.END, '\n'.join(sorted_dates_str))

                self.time_label.config(text=f"Tiempo de Ejecución (Quick Sort): {time:.4f} segundos")
        else:
            messagebox.showwarning("Advertencia", "No se han ingresado fechas para ordenar.")

    def sort_dates_merge(self):
        if len(self.dates) > 0:
            setup_code = f"from __main__ import merge_sort; dates = {self.dates}"
            stmt = "sorted_dates = merge_sort(dates.copy())"
            time = timeit.timeit(stmt, setup=setup_code, number=100, globals=globals())

            sorted_dates = merge_sort(self.dates.copy())
            if sorted_dates is not None:
                sorted_dates_str = [date.strftime('%Y-%m-%d') for date in sorted_dates]
                self.sorted_dates_text.delete(1.0, tk.END)
                self.sorted_dates_text.insert(tk.END, '\n'.join(sorted_dates_str))

                self.time_label.config(text=f"Tiempo de Ejecución (Merge Sort): {time:.4f} segundos")
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
