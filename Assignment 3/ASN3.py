import tkinter as tk
from tkinter import messagebox

def display_data():
    """Event handler for the Submit button."""
    first = entFirst.get().strip()
    last = entLast.get().strip()
    email = entEmail.get().strip()
    phone = entPhone.get().strip()

    # Simple validation to ensure required fields aren't empty
    if not first or not last:
        messagebox.showwarning("Input Error", "First and Last Name are required.")
        return

    # Formatting the output message
    output = f"You enterd:\nName: {first} {last}\nEmail: {email}\nPhone: {phone}"
    messagebox.showinfo(f"Welcome to tkinter, {first}", output)

def clear_fields():
    """Event handler for the Reset button."""
    entFirst.delete(0, tk.END)
    entLast.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entPhone.delete(0, tk.END)
    entFirst.focus_set()

# --- Main Form Setup ---
root = tk.Tk()
root.title("tkinter Form")
root.geometry("500x300")


# Branding configuration
branding = {"bg": "blue", "fg": "white"}

# --- Personal Information LabelFrame ---
lblFrPerson = tk.LabelFrame(root, text="Personal Information", padx=10, pady=10)
lblFrPerson.pack(padx=20, pady=10, fill="both", expand=True)

# First Name
lblFirst = tk.Label(lblFrPerson, text="*First Name:", **branding)
lblFirst.grid(column=0, row=0, sticky="w", padx=5, pady=2)
entFirst = tk.Entry(lblFrPerson)
entFirst.grid(column=1, row=0, sticky="ew", padx=5, pady=2)

# Last Name
lblLast = tk.Label(lblFrPerson, text="*Last Name:", **branding)
lblLast.grid(column=0, row=1, sticky="w", padx=5, pady=2)
entLast = tk.Entry(lblFrPerson)
entLast.grid(column=1, row=1, sticky="ew", padx=5, pady=2)

# Email
lblEmail = tk.Label(lblFrPerson, text="Email:")
lblEmail.grid(column=0, row=2, sticky="w", padx=5, pady=2)
entEmail = tk.Entry(lblFrPerson)
entEmail.grid(column=1, row=2, sticky="ew", padx=5, pady=2)

# Phone
lblPhone = tk.Label(lblFrPerson, text="Phone:")
lblPhone.grid(column=0, row=3, sticky="w", padx=5, pady=2)
entPhone = tk.Entry(lblFrPerson)
entPhone.grid(column=1, row=3, sticky="ew", padx=5, pady=2)

# Configure grid weight so entry boxes expand
lblFrPerson.columnconfigure(1, weight=1)

# --- Button Frame ---
fraButtons = tk.Frame(root)
fraButtons.pack(pady=10)

btnS = tk.Button(fraButtons, text="Submit", width=5, command=display_data)
btnS.pack(side=tk.LEFT, padx=5)

btnR = tk.Button(fraButtons, text="Reset", width=5, command=clear_fields)
btnR.pack(side=tk.LEFT, padx=5)

btnQ = tk.Button(fraButtons, text="Quit", width=5, command=root.destroy)
btnQ.pack(side=tk.LEFT, padx=5)

root.mainloop()
