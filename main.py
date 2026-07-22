import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# --- Initialize App ---
root = tk.Tk()
root.title("5-Time Prayer Tracker")
root.geometry("400x500")

# --- Variables ---
records = []

# --- Get Username ---
tk.Label(root, text="Enter your name:").pack()
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# --- Prayer Checkboxes ---
prayer_vars = []
masjid_vars = []
prayer_names = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

tk.Label(root, text="Select prayers you prayed:").pack()
for prayer in prayer_names:
    p_var = tk.IntVar()
    m_var = tk.IntVar()
    tk.Checkbutton(root, text=prayer, variable=p_var).pack(anchor='w')
    tk.Checkbutton(root, text=f"At Masjid ({prayer})", variable=m_var).pack(anchor='w', padx=20)
    prayer_vars.append(p_var)
    masjid_vars.append(m_var)

# --- Save Function ---
def save_record():
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning("Input Error", "Please enter your name.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    with open("namaz.txt", "a") as f:
        f.write("-"*50 + "\n")
        f.write(f"Date: {today}\n")
        f.write(f"Name: {name}\n")
        for i, prayer in enumerate(prayer_names):
            status = "Prayed" if prayer_vars[i].get() else "Missed"
            place = " (Masjid)" if masjid_vars[i].get() else " (Home)"
            if prayer_vars[i].get():
                f.write(f"{prayer}: {status}{place}\n")
            else:
                f.write(f"{prayer}: {status}\n")
        f.write("\n")

    messagebox.showinfo("Saved", "Today's record saved to namaz.txt")
    # Reset checkboxes
    for var in prayer_vars + masjid_vars:
        var.set(0)

# --- Save Button ---
tk.Button(root, text="Save Today's Record", command=save_record, bg="green", fg="white").pack(pady=20)

# --- Run App ---
root.mainloop()
