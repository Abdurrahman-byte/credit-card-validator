from tkinter import *


total = 0

def validate():

    sum_odd_digits = 0
    sum_even_digits = 0


    card_number = entry.get()
    card_number = card_number.replace("-", "")
    card_number = card_number.replace(" ", "")
    card_number = card_number[::-1]

    for x in card_number[::2]:
        sum_odd_digits += int(x)

    for x in card_number[1::2]:
        x = int(x) * 2
        if x >= 10:
            sum_even_digits += (1 +(x % 10))
        else:
            sum_even_digits += x

    total = sum_odd_digits + sum_even_digits

    if total % 10 == 0:
        label.config(text="VALID CARD", fg="green")
    else:
        label.config(text="INVALID CARD", fg="red")



window = Tk()

window.title("Card Validator")
window.geometry("300x150")

entry = Entry(window, font=("Arial", 10))
entry.pack(pady=10)

button = Button(window, text="Validate", command=validate)
button.pack(pady=5)

label = Label(window, text="Enter a card number", font=("consolas", 10))
label.pack(pady=10)

window.mainloop()