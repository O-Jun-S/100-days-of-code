import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)


# Button
def button_clicked():
    my_label["text"] = "I got clicked!"


my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button.grid(row=1, column=1)

new_button = tkinter.Button(text="New button")
new_button.grid(row=0, column=2)

# Entry
entry = tkinter.Entry(width=10)
entry.grid(row=2, column=3)

window.mainloop()
