from tkinter import ttk
from ttkthemes import ThemedTk

running = False
h = 0
m = 0
s = 0


def counter_label(label):
    def count():
        global h, m, s
        if running:
            if s == 60:
                s = 0
                m += 1
            if m == 60:
                m = 0
                h += 1

            s_str = str(s).zfill(2)
            m_str = str(m).zfill(2)
            h_str = str(h).zfill(2)

            display = f"Hours: {h_str}"
            display2 = f"Minutes: {m_str}"
            display3 = f"Seconds: {s_str}"

            label.config(text=display)
            label2.config(text=display2)
            label3.config(text=display3)

            s += 1
            label.after(1000, count)

    count()


def Start(label):
    global running
    running = True
    counter_label(label)
    start.config(state='disabled')
    stop.config(state='normal')
    reset.config(state='normal')


def Stop():
    global running
    running = False
    start.config(state='normal')
    stop.config(state='disabled')


def Reset(label):
    global h, m, s
    h = 0
    m = 0
    s = 0

    label.config(text="Hours: 00")
    label2.config(text="Minutes: 00")
    label3.config(text="Seconds: 00")

    start.config(state='normal')
    stop.config(state='disabled')
    reset.config(state='disabled')


root = ThemedTk(theme="yaru")
root.title("Stopwatch")

start_title1 = "Hours: 00"
start_title2 = "Minutes: 00"
start_title3 = "Seconds: 00"

label = ttk.Label(root, text=start_title1, foreground="black", font="Courier 30 italic", anchor='w')
label.pack(fill='both')

label2 = ttk.Label(root, text=start_title2, foreground="black", font="Courier 30 italic", anchor='w')
label2.pack(fill='both')

label3 = ttk.Label(root, text=start_title3, foreground="black", font="Courier 30 italic", anchor='w')
label3.pack(fill='both')

f = ttk.Frame(root)

start = ttk.Button(f, text='Start', width=6, command=lambda: Start(label))
stop = ttk.Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = ttk.Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))
f.pack(anchor='center', pady=5)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")

root.mainloop()
