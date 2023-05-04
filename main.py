from tkinter import *


window = Tk()
window.title("Kalkulačka složeného úročení verze 1.0.0")
window.minsize(600, 250)
window.resizable(True, True)

amount_label = Label(text="Investovaná částka:", font=("Arial", 20))
amount_label.grid(row=0, column=0, padx=10, pady=10)

user_amount_input = Entry(width=10, font=("Arial", 20), justify=RIGHT)
user_amount_input.insert(0, "")
user_amount_input.grid(row=0, column=1, padx=10, pady=25)

currency_drop_down = StringVar(window)
currency_drop_down.set("CZK")
currency_drop_down_set = OptionMenu(window, currency_drop_down, "CZK", "EUR", "USD")
currency_drop_down_set.grid(row=0, column=2, padx=10, pady=25)

interest_rate_label = Label(text="Roční úroková sazba:", font=("Arial", 20))
interest_rate_label.grid(row=1, column=0, padx=10, pady=(10, 0))

user_interest_rate_input = Entry(width=10, font=("Arial", 20), justify=RIGHT)
user_interest_rate_input.insert(0, "")
user_interest_rate_input.grid(row=1, column=1, padx=10, pady=25)

num_of_years_label = Label(text="Počet let:", font=("Arial", 20))
num_of_years_label.grid(row=2, column=0, padx=10, pady=10)

user_years_input = Entry(width=10, font=("Arial", 20), justify=RIGHT)
user_years_input.insert(0, "")
user_years_input.grid(row=2, column=1, padx=10, pady=25)

count_button = Button(window, text="Spočítej", font=("Arial", 20))
count_button.grid(row=3, column=1, padx=10, pady=10)

result_label = Label(text="Konečná částka:", font=("Arial", 20))
result_label.grid(row=4, column=0, padx=10, pady=10)

final_amount_label = Label(text="0", fg="black", font=("Arial", 20))
final_amount_label.grid(row=4, column=1)

window.mainloop()