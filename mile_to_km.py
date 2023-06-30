from tkinter import *

result = "0"


def update_result():
    global result
    result = round(float(miles_entry.get()) * 1.609344, 2)
    result_label.config(text=result)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=290, height=100)
window.config(padx=30, pady=30)

# Entry
miles_entry = Entry(width=10)
miles_entry.focus()
print(miles_entry.get())
miles_entry.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles", font=("Arial", 12, "normal"))
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to", font=("Arial", 12, "normal"))
equal_to_label.grid(column=0, row=1)

result_label = Label(text=result, font=("Arial", 12, "normal"))
result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 12, "normal"))
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=update_result)
button.grid(column=1, row=2)

window.mainloop()
