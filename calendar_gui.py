from tkinter import *
import calendar

# root window setup
root = Tk()
root.geometry("350x320")
root.title("📅 Stylish Calendar")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Function to display calendar
def show():
    a = int(spin_month.get())
    b = int(spin_year.get())
    cal = calendar.month(b, a)
    txt.delete(0.0, END)
    txt.insert(INSERT, cal)

# Top title
Label(root, text="Monthly Calendar", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)

# Frame for input controls
frame = Frame(root, bg="#e1f5fe", bd=2, relief=RIDGE)
frame.pack(pady=5)

Label(frame, text="Month", font=('Arial', 10, 'bold'), bg="#e1f5fe", fg="#000").grid(row=0, column=0, padx=10, pady=10)
Label(frame, text="Year", font=('Arial', 10, 'bold'), bg="#e1f5fe", fg="#000").grid(row=0, column=2, padx=10)

# Spinboxes
spin_month = Spinbox(frame, values=tuple(range(1, 13)), width=5, font=('Arial', 10))
spin_year = Spinbox(frame, from_=1999, to=2100, width=7, font=('Arial', 10))
spin_month.grid(row=0, column=1)
spin_year.grid(row=0, column=3)

# Show button
def on_enter(e): btn_show.config(bg="#0288d1", fg="white")
def on_leave(e): btn_show.config(bg="#03a9f4", fg="black")

btn_show = Button(root, text="Show Calendar", font=('Arial', 11, 'bold'), bg="#03a9f4", fg="black", command=show, bd=2, relief=RAISED, cursor="hand2")
btn_show.pack(pady=10)
btn_show.bind("<Enter>", on_enter)
btn_show.bind("<Leave>", on_leave)

# Text area for displaying calendar
txt = Text(root, width=33, height=10, font=("Courier", 10), bd=2, relief=GROOVE, bg="#fff3e0")
txt.pack(pady=5)

root.mainloop()
