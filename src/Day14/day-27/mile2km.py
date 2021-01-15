import tkinter

FONT = ("Arial", 15, "bold")

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)

# mile text box.
text_input = tkinter.Entry(width=15)
text_input.grid(row=0, column=1)

# display "Miles"
label_mile = tkinter.Label(text="Miles", font=FONT)
label_mile.grid(row=0, column=2)

# display "is equal to"
label_equal = tkinter.Label(text="is equal to", font=FONT)
label_equal.grid(row=1, column=0)

# display result of convert
result = tkinter.Label(text="0", font=FONT)
result.grid(row=1, column=1)

# display "Km"
label_km = tkinter.Label(text="Km", font=FONT)
label_km.grid(row=1, column=2)


# calculate button
def calc():
    miles = int(text_input.get())
    kilos = miles * 1.609
    result["text"] = str(kilos)


calc_button = tkinter.Button(text="Calculate", font=FONT,
                             command=calc)
calc_button.grid(row=2, column=1)

window.mainloop()
