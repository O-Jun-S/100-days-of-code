import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
OUTPUT_FILE = "efforts.txt"
reps = 0
with open(OUTPUT_FILE) as file:
    efforts = int(file.read())
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global efforts
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        efforts = work_sessions
        efforts_label.config(text=f"You made {efforts} efforts!")
        save_efforts()
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)


# ----------------------------- FILE I/O ------------------------- #
def save_efforts():
    global efforts
    print("saving")
    with open(OUTPUT_FILE, "w") as save_file:
        save_file.write(str(efforts))


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = tkinter.Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato)
timer_text = canvas.create_text(100, 130,
                                text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW,
                            font=(FONT_NAME, 35, "bold"))
title_label.grid(row=0, column=1)

start_button = tkinter.Button(text="Start", width=5,
                              bg="white", command=start_timer,
                              font=(FONT_NAME, 10, "bold"))
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", width=5,
                              bg="white", command=reset_timer,
                              font=(FONT_NAME, 10, "bold"))
reset_button.grid(row=2, column=2)

check_marks = tkinter.Label(fg=GREEN, bg=YELLOW,
                            font=(FONT_NAME, 15, "bold"))
check_marks.grid(row=3, column=1)

efforts_label = tkinter.Label(text=f"You made {efforts} efforts!",
                              fg=PINK, bg=YELLOW,
                              font=(FONT_NAME, 15, "bold"))
efforts_label.grid(row=4, column=1)

window.mainloop()
