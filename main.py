from tkinter import *
from tkinter import messagebox


window = Tk()
message = messagebox
currencies = ["CZK", "EUR", "USD"]
window.title("Kalkulačka složeného úročení verze 1.0.0")
window.geometry("500x400+1000+20")
window.resizable(True, True)

def count_result():
    try:
        amount = int(user_amount_input.get())
        percent = float(user_interest_rate_input.get())
        years = int(user_years_input.get())
        currency = currency_drop_down.get()
        result = amount * (1 + percent / 100) ** years
        final_amount_label.config(text=round(result, 2))
        currency_label.config(text=currency)
    except:
        message.showinfo(title="Upozornění", message="Zadej všechny hodnoty!")

def delete_inputs():
    user_amount_input.delete(0, END)
    user_interest_rate_input.delete(0, END)
    user_years_input.delete(0, END)
    final_amount_label.config(text="0")

amount_label = Label(text="Investovaná částka:", font=("Arial", 20))
amount_label.grid(row=0, column=0, padx=10, pady=10)

user_amount_input = Entry(width=10, font=("Arial", 20), justify=RIGHT)
user_amount_input.insert(0, "")
user_amount_input.grid(row=0, column=1, padx=10, pady=25)

currency_drop_down = StringVar(window)
currency_drop_down.set(currencies[0])
currency_drop_down_set = OptionMenu(window, currency_drop_down, *currencies)
currency_drop_down_set.grid(row=0, column=2, padx=10, pady=25)

interest_rate_label = Label(text="Roční úroková sazba:", font=("Arial", 20))
interest_rate_label.grid(row=1, column=0, padx=10, pady=(10, 0))

user_interest_rate_input = Entry(width=10, font=("Arial", 20), justify=RIGHT)
user_interest_rate_input.insert(0, "")
user_interest_rate_input.grid(row=1, column=1, padx=10, pady=25)

percent_label = Label(text="%", fg="black", font=("Arial", 20))
percent_label.grid(row=1, column=2)

num_of_years_label = Label(text="Počet let:", font=("Arial", 20))
num_of_years_label.grid(row=2, column=0, padx=10, pady=10)

user_years_input = Entry(width=10, font=("Arial", 20), justify=RIGHT)
user_years_input.insert(0, "")
user_years_input.grid(row=2, column=1, padx=10, pady=25)

count_button = Button(window, text="Spočítej", font=("Arial", 20), command=count_result)
count_button.grid(row=3, column=1, padx=10, pady=10)

delete_button = Button(window, text="Smazat", font=("Arial", 20), command=delete_inputs)
delete_button.grid(row=3, column=2, padx=10, pady=10)

result_label = Label(text="Konečná částka:", font=("Arial", 20))
result_label.grid(row=4, column=0, padx=10, pady=10)

final_amount_label = Label(text="0", fg="black", font=("Arial", 20))
final_amount_label.grid(row=4, column=1)

currency_label = Label(text="", fg="black", font=("Arial", 20))
currency_label.grid(row=4, column=2)

window.mainloop()