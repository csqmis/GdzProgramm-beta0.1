import tkinter as tk
from tkinter import messagebox

# Создаем главное окно
root = tk.Tk()
root.title("ГДЗ - Выбор задания")
root.geometry("500x400")

# Переменные
class_var = tk.StringVar()
subject_var = tk.StringVar()
link_var = tk.StringVar()

# Функция для заполнения предметов
def fill_subjects():
    # Очистка области предметов
    for widget in frame_subjects.winfo_children():
        widget.destroy()

    selected_class = class_var.get()

    if selected_class == '7':
        # Добавляем предмет
        subject_label = tk.Label(frame_subjects, text="Выберите предмет:")
        subject_label.pack(anchor='w', pady=5)

        algebra_radio = tk.Radiobutton(frame_subjects, text='Алгебра', variable=subject_var, value='algebra')
        algebra_radio.pack(anchor='w')

        # Активировать кнопку продолжения
        continue_button.config(state='normal')
    else:
        messagebox.showinfo("Информация", "Этот класс не поддерживается или программа не настроена для другого класса.")
        continue_button.config(state='disabled')

def show_link():
    if subject_var.get() == '':
        messagebox.showwarning("Предупреждение", "Пожалуйста, выберите предмет.")
        return
    try:
        zadanie_num = int(entry_zadanie.get())
        if not (1 <= zadanie_num <= 1247):
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректный номер задания (от 1 до 1247).")
        return

    url = f'https://gdz.ru/class-7/algebra/makarichev-18/{zadanie_num}-task/'
    link_var.set(url)

# Заголовок выбора класса
label_class = tk.Label(root, text="Выберите ваш класс:")
label_class.pack(pady=5)

# Область с радиокнопками для класса, без начального выбора
class_frame = tk.Frame(root)
class_frame.pack()

# Радиокнопка "7 класс" без выбранного состояния по умолчанию
radio_7 = tk.Radiobutton(class_frame, text='7 класс', variable=class_var, value='7', command=fill_subjects)
radio_7.pack(anchor='w')

# Область для выбора предметов
frame_subjects = tk.Frame(root)
frame_subjects.pack(pady=10)

# Ввод номера задания
label_zadanie = tk.Label(root, text="Введите номер задания (от 1 до 1247):")
label_zadanie.pack()

entry_zadanie = tk.Entry(root)
entry_zadanie.pack()

# Кнопка для отображения ссылки
continue_button = tk.Button(root, text="Показать ссылку", command=show_link, state='disabled')
continue_button.pack(pady=10)

# Метка для отображения ссылки
link_label = tk.Label(root, textvariable=link_var, fg='blue', cursor='hand2')
link_label.pack(pady=5)

def open_link(event):
    import webbrowser
    webbrowser.open(link_var.get())

link_label.bind("<Button-1>", open_link)

root.mainloop()