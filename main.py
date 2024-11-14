import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import random

def generate_file():
    """
    Открывает диалоговое окно для выбора пути сохранения файла.
    Запрашивает у пользователя количество чисел для генерации.
    Генерирует случайные числа в диапазоне от 1 до 100 и записывает их в файл.
    Отображает сообщение об успешном создании файла.
    """
    filepath = filedialog.asksaveasfilename(defaultextension=".txt")
    if filepath:
        try:
            number_count = int(number_entry.get())
            with open(filepath, "w") as file:
                for el in range(number_count):
                    file.write(str(random.randint(1, 100)) + "\n")
            messagebox.showinfo("Успех", f"Файл '{filepath}' создан с {number_count} случайных чисел.")
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат количества чисел.")

def read_and_calculate(filepath):
    """
    Открывает файл для чтения.
    Считывает числа из файла и преобразует их в целые числа.
    Вычисляет среднее значение чисел.
    Формирует строку с содержимым файла и средним значением.
    Отображает результат в диалоговом окне.
    """
    try:
        with open(filepath, "r") as file:
            numbers = [int(line) for line in file]
            average = sum(numbers) / len(numbers)
            result = f"Содержимое файла:\n" + "\n".join(str(number) for number in numbers) + f"\n\nСреднее значение: {average}"
            messagebox.showinfo("Результат", result)
    except FileNotFoundError:
        messagebox.showerror("Ошибка", f"Файл '{filepath}' не найден.")

def read_file():
    """
    Открывает диалоговое окно для выбора файла.
    Вызывает функцию read_and_calculate для обработки выбранного файла.
    """
    filepath = filedialog.askopenfilename(defaultextension=".txt")
    if filepath:
        read_and_calculate(filepath)

def multiply():
    try:
        a = int(a_value.get())
        b = int(b_value.get())
        messagebox.showinfo(f"Результат", f"Умножение равно: {a * b}")
    except ValueError:
        messagebox.showerror("Ошибка", "Вы не ввели числа")

def div(a, b):
    if(b != 0):
        return a / b
    else:
        return "Делить на 0 нельзя!!!"

def division():
    try:
        a = int(a_value.get())
        b = int(b_value.get())
        messagebox.showinfo(f"Результат", f"Деление равно: {div(a, b)}")
    except ValueError:
        messagebox.showerror("Ошибка", "Вы не ввели числа")

def addition():
    try:
        a = int(a_value.get())
        b = int(b_value.get())
        messagebox.showinfo(f"Результат", f"Сложение равно: {a + b}")
    except ValueError:
        messagebox.showerror("Ошибка", "Вы не ввели числа")

def subtract():
    try:
        a = int(a_value.get())
        b = int(b_value.get())
        messagebox.showinfo(f"Результат", f"Вычетание равно: {a - b}")
    except ValueError:
        messagebox.showerror("Ошибка", "Вы не ввели числа")

def exponentiaton():
    try:
        a = int(a_value.get())
        b = int(b_value.get())
        messagebox.showinfo(f"Результат", f"Возведение в степень равно: {a ** b}")
    except ValueError:
        messagebox.showerror("Ошибка", "Вы не ввели числа")


root = tk.Tk()
root.title("Обработка случайных чисел")
root.geometry("220x400")

style = ttk.Style()
style.configure("TButton", padding=2, background="#F08080")

root.grid_rowconfigure(3, minsize=10)
root.grid_rowconfigure(5, minsize=15)
root.grid_rowconfigure(8, minsize=15)
root.grid_rowconfigure(10, minsize=20)
root.grid_rowconfigure(12, minsize=15)
root.grid_rowconfigure(14, minsize=15)
root.grid_rowconfigure(16, minsize=15)
root.grid_rowconfigure(18, minsize=15)
root.grid_rowconfigure(20, minsize=15)

number_label = tk.Label(root, text="Введите количество чисел:")
number_label.grid(row=2, column=0)
number_entry = tk.Entry(root, width=10)
number_entry.grid(row=2, column=1)

generate_button = ttk.Button(root, text="Создать файл", command=generate_file, style="TButton")
generate_button.grid(row=4, column=0, columnspan=2, sticky="ew")

read_button = ttk.Button(root, text="Прочитать файл", command=read_file, style="TButton")
read_button.grid(row=6, column=0, columnspan=2, sticky="ew")

number_value = tk.Label(root, text="Введите два числа:")
number_value.grid(row=7, column=0)
a_value = tk.Entry(root, width=10)
a_value.grid(row=9, column=0)
b_value = tk.Entry(root, width=10)
b_value.grid(row=9, column=1)

multiply_button = ttk.Button(root, text="Умножить", command=multiply, style="TButton")
multiply_button.grid(row=11, column=0, columnspan=2, sticky="ew")

division_button = ttk.Button(root, text="Делить", command=division, style="TButton")
division_button.grid(row=13, column=0, columnspan=2, sticky="ew")

addition_button = ttk.Button(root, text="Сложить", command=addition, style="TButton")
addition_button.grid(row=15, column=0, columnspan=2, sticky="ew")

subtract_button = ttk.Button(root, text="Вычесть", command=subtract, style="TButton")
subtract_button.grid(row=17, column=0, columnspan=2, sticky="ew")

exponentiaton_button = ttk.Button(root, text="Возвести в степень", command=exponentiaton, style="TButton")
exponentiaton_button.grid(row=19, column=0, columnspan=2, sticky="ew")

root.mainloop()