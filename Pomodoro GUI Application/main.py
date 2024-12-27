from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

PHOTO_IMAGE_PATH = "Python Bootcamp/Intermediate/Pomodoro GUI Application/tomato.png"

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    if timer:
        window.after_cancel(timer)
        canvas.itemconfig(c_text, text="00:00")
        lbl_timer.config(text="Timer", fg=GREEN)
        lbl_repeats.config(text="")
        global reps
        reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        lbl_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        lbl_timer.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        lbl_timer.config(text="Work", fg=GREEN)

    if reps == 8:
        reps = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(time_in_secs):

    minutes = time_in_secs // 60
    seconds = time_in_secs % 60
    
    if seconds < 10:
        seconds = f"0{seconds}"

    timer_value = f"{minutes}:{seconds}"
    canvas.itemconfig(c_text, text=timer_value)

    if time_in_secs > 0:
        global timer
        timer = window.after(1000, count_down, time_in_secs - 1)
    else:
        start_timer()
        marks = "✓" * (reps // 2)
        lbl_repeats.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=150, pady=50, bg=YELLOW)
window.geometry(f"+800+300")

lbl_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=("Courier", 50, "normal"))
lbl_timer.grid(row=0, column=1)

tomato_img = PhotoImage(file=PHOTO_IMAGE_PATH)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
c_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

btn_start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
btn_start.grid(row=2, column=0)

btn_reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
btn_reset.grid(row=2, column=2)

lbl_repeats = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "normal"))
lbl_repeats.grid(row=3, column=1)

window.mainloop()