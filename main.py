import tkinter as tk
import random
import string
import pyperclip  # Импортируем библиотеку pyperclip


# Функция для генерации пароля
def generate_password(length, use_digits, use_symbols):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Функция для генерации пароля и отображения
def generate_password_and_display():
    length = int(length_entry.get())  # Получаем длину пароля из текстового поля.
    use_digits = digits_var.get()  # Получаем выбор пользователя по цифрам.
    use_symbols = symbols_var.get()  # Получаем выбор пользователя по символам.

    password = generate_password(length, use_digits, use_symbols)  # Генерируем пароль.
    result_label.config(text="Сгенерированный пароль: " + password)  # Отображаем пароль.

    # Копируем сгенерированный пароль в буфер обмена
    pyperclip.copy(password)
    result_label.config(
        text=result_label.cget("text") + " (скопирован в буфер обмена)")  # Отображаем сообщение о копировании


# Создаем главное окно
root = tk.Tk()
root.title("Генератор паролей")

# Создаем элементы интерфейса
length_label = tk.Label(root, text="Длина пароля:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

digits_var = tk.BooleanVar()
digits_checkbutton = tk.Checkbutton(root, text="Включить цифры", variable=digits_var)
digits_checkbutton.pack()

symbols_var = tk.BooleanVar()
symbols_checkbutton = tk.Checkbutton(root, text="Включить специальные символы", variable=symbols_var)
symbols_checkbutton.pack()

generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_password_and_display)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Запускаем главный цикл
root.mainloop()
