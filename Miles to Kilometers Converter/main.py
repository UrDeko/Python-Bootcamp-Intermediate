from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

def click_convert():
    miles = input.get()

    if miles:
        to_kilometers = int(miles) * 1.609
        lbl_result.config(text=f"{to_kilometers}")
    else:
        lbl_result.config(text="0")

lbl_intro = Label(text="Miles to\nKilometers\nConverter", font=("Courier", 20, "bold"))
lbl_intro.grid(rowspan=2, column=0)

input = Entry()
input.grid(row=0, column=1, padx=20, pady=20)
input.config(width=5)

lbl_miles = Label(text="Miles")
lbl_miles.grid(row=0, column=2, padx=20, pady=5)

lbl_result = Label(text="0")
lbl_result.grid(row=1, column=1, padx=20, pady=5)

lbl_kilometers = Label(text="Kilometers")
lbl_kilometers.grid(row=1, column=2, padx=20, pady=5)

btn_convert = Button(text="Convert", command=click_convert)
btn_convert.grid(row=2, columnspan=3, padx=20, pady=5)
btn_convert.config(width=40)

window.mainloop()