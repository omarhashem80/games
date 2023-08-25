import tkinter as t
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
mark = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_count():
    global rep
    window.after_cancel(timer)
    rep = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label['text'] = "Timer"
    check_label['text'] = ""
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_count():
    global rep, mark
    rep += 1
    if rep % 2 and rep < 8:
        timer_label['text'] = "Work"
        timer_label['fg'] = GREEN
        count_down(WORK_MIN*60)
    elif rep == 8:
        timer_label['text'] = "Break"
        timer_label['fg'] = RED
        count_down(LONG_BREAK_MIN*60)
    elif rep % 2 == 0:
        timer_label['text'] = "Break"
        timer_label['fg'] = PINK
        count_down(SHORT_BREAK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global rep
    minute = f"{count//60}"
    sec = f"{count%60}"
    if len(sec) == 1:
        sec = "0"+sec
    if len(minute) == 1:
        minute = "0"+minute
    canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_count()
        if rep and rep % 2 == 0:
            check_label['text'] = mark * (rep//2)


# ---------------------------- UI SETUP ------------------------------- #


window = t.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

t_image = t.PhotoImage(file="./tomato.png")

canvas = t.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=t_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)


timer_label = t.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_label.grid(row=0, column=1)

check_label = t.Label(bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)


start_button = t.Button(text="Start", highlightthickness=0, command=start_count)
start_button.grid(row=2, column=0)

reset_button = t.Button(text="Reset", highlightthickness=0, command=reset_count)
reset_button.grid(row=2, column=2)

window.mainloop()
