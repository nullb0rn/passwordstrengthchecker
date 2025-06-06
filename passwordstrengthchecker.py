import tkinter as tk
import string
import random

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def check_strength():
    password = entry.get()

    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    if score == 5:
        result.set("🟢 Very Strong")
        suggestion.set("")
    elif score == 4:
        result.set("🟡 Strong")
        suggestion.set("")
    elif score == 3:
        result.set("🟠 Medium")
        suggestion.set("Try adding a symbol or uppercase letter.")
    else:
        result.set("🔴 Weak")
        suggestion.set("Try this strong password: " + generate_password())

window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("350x250")
window.resizable(False, False)

tk.Label(window, text="Enter Password:").pack(pady=10)

entry = tk.Entry(window, show="*", width=30)
entry.pack()

result = tk.StringVar()
tk.Label(window, textvariable=result, font=("Arial", 12, "bold")).pack()

suggestion = tk.StringVar()
tk.Label(window, textvariable=suggestion, wraplength=300, fg="gray").pack(pady=5)

tk.Button(window, text="Check Strength", command=check_strength).pack(pady=10)

window.mainloop()
