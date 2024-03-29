import re
import tkinter as tk


def validate_email():
    email = entry_email.get()

    if "@" not in email:
        result = "Invalid email: Missing '@' ."
        color = "red"

    elif "." not in email:
        result = "Invalid email: Missing '.' ."
        color = "red"

    else:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, email):
            result = "Email is Valid!"
            color = "green"
        else:
            result = "Invalid email. Contains forbidden characters or wrong format."
            color = "red"

    entry_result.delete(0, tk.END)
    entry_result.insert(0, result)
    entry_result.config(fg=color)


root = tk.Tk()
root.geometry("500x500")
root.title("Email Validator")

label_instructions = tk.Label(root, text="Enter an email address. it should include '@' and '.domain'")
label_instructions.pack()

entry_email = tk.Entry(root, width=70)
entry_email.pack()
entry_email.delete(0, tk.END)

button_validate = tk.Button(root, text="Validate Email", command=validate_email)
button_validate.pack()

entry_result = tk.Entry(root, width=70)
entry_result.pack()
entry_result.delete(0, tk.END)

root.mainloop()