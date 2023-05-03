from tkinter import *


window = Tk()
window.title("Kalkulačka složeného úročení verze 1.0.0")
window.minsize(600, 250)
window.resizable(True, True)

amount_label = Label(text="Investovaná částka:", font=("Arial", 20))
amount_label.grid(row=0, column=0, padx=10, pady=10)

interest_rate_label = Label(text="Roční úroková sazba:", font=("Arial", 20))
interest_rate_label.grid(row=1, column=0, padx=10, pady=10)

num_of_years_label = Label(text="Počet let:", font=("Arial", 20))
num_of_years_label.grid(row=2, column=0, padx=10, pady=10)

result_label = Label(text="Konečná částka:", font=("Arial", 20))
result_label.grid(row=3, column=0, padx=10, pady=10)

user_amount_input = Entry(width=10, font=("Arial", 20), justify=RIGHT)
user_amount_input.insert(0, "")
user_amount_input.grid(row=0, column=1, padx=10, pady=25)

user_interest_rate_input = Entry(width=10, font=("Arial", 20), justify=RIGHT)
user_interest_rate_input.insert(0, "")
user_interest_rate_input.grid(row=1, column=1, padx=10, pady=25)

user_years_input = Entry(width=10, font=("Arial", 20), justify=RIGHT)
user_years_input.insert(0, "")
user_years_input.grid(row=2, column=1, padx=10, pady=25)

final_amount_label = Label(text="0", fg="black", font=("Arial", 20))
final_amount_label.grid(row=3, column=1)

window.mainloop()