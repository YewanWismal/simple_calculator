import tkinter as tk

calc = ""

def update():
    entry.config(state="normal")
    entry.delete(0, "end")
    entry.insert("end", calc)
    entry.config(state="readonly")

def press(key):
    global calc
    if key == "=":
        try:
            calc = str(eval(calc))
        except:
            calc = "Error"
    elif key == "C":
        calc = ""
    else:
        calc += key
    update()

def handle(key):
    global calc
    if key == "⌫":
        calc = calc[:-1]
    elif key == "÷":
        calc += "/"
    elif key == "×":
        calc += "*"
    elif key == "√":
        try:
            calc = str(eval(f"({calc})**0.5"))
        except:
            calc = "Error"
    elif key == "1/x":
        try:
            calc = str(1 / float(calc))
        except:
            calc = "Error"
    elif key == "x²":
        try:
            calc = str(float(calc) ** 2)
        except:
            calc = "Error"
    elif key == "±":
        try:
            if calc.startswith("-"):
                calc = calc[1:]
            else:
                calc = "-" + calc
        except:
            calc = "Error"
    elif key == "CE":
        calc = ""
    else:
        press(key)
    update()

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

entry = tk.Entry(root, font=("Segoe UI", 30), bg="#1e1e1e", fg="white",
                 bd=0, justify="right", insertbackground="white",
                 readonlybackground="#1e1e1e", state="readonly")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

buttons = [
    ["%", "CE", "C", "⌫"],
    ["1/x", "x²", "√", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["±", "0", ".", "="]
]

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        b = tk.Button(root, text=char, font=("Segoe UI", 16), fg="white", bg="#2d2d2d",
                      activebackground="#3a3a3a", activeforeground="white", bd=0,
                      command=lambda k=char: handle(k))
        b.grid(row=r + 1, column=c, sticky="nsew", padx=4, pady=4, ipadx=10, ipady=10)

for i in range(6 + 1):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.geometry("400x550")
root.mainloop()
