import tkinter as tk
from enemycheck import get_data, clear_vers_entries, fill_data, format_realm, name_entries, vers_entries

# Initiate window
window = tk.Tk()

# Create main label for the window


main_label = tk.Label(text="Welcome to Weakest Link")
main_label.grid(row=0, column=1)

# Create 10 input fields for data and output


for i in range(0, 10):
    tk.Label(window, text=f"Enemy {i+1}").grid(row=i+1)
    inputname = str('name'+str(i+1))
    inputname = tk.Entry(window)
    inputname.grid(row=i+1, column=1)
    name_entries.append(inputname)

for i in range(0, 10):
    inputname = str('vers'+str(i+1))
    inputname = tk.Entry(window)
    inputname.grid(row=i+1, column=2)
    vers_entries.append(inputname)


# Create the start button


button = tk.Button(window, text="Find the weakest link!", width=16, height=1, command=fill_data)
button.grid(row=11, column=1)

window.mainloop()
