import tkinter as tk
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

root = tk.Tk()
root.title("Обработка случайных чисел")
root.geometry("300x150")

root.grid_rowconfigure(3, minsize=10)
root.grid_rowconfigure(5, minsize=15)

number_label = tk.Label(root, text="Введите количество чисел:")
number_label.grid(row=2, column=0)
number_entry = tk.Entry(root, width=10)
number_entry.grid(row=2, column=1)

generate_button = tk.Button(root, text="Создать файл", command=generate_file)
generate_button.grid(row=4, column=0, columnspan=2, sticky="ew")

read_button = tk.Button(root, text="Прочитать файл", command=read_file)
read_button.grid(row=6, column=0, columnspan=2, sticky="ew")

root.mainloop()