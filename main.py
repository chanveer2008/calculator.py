import tkinter as tk
from tkinter import ttk
import threading
import time

def open_calculator():
    loading_window.destroy()
    root.deiconify()

def show_loading_screen():
    global loading_window
    loading_window = tk.Tk()
    loading_window.title("Loading...")
    label = tk.Label(loading_window, text="TechnoSolution", font=("Arial", 20))
    label.pack(pady=20)
    progress = ttk.Progressbar(loading_window, orient='horizontal', mode='indeterminate')
    progress.pack(pady=10)
    progress.start()
    loading_window.after(2000, open_calculator)
    loading_window.mainloop()

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif text == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, text)

root = tk.Tk()
root.withdraw()  # Hide the main window initially

keys = [
    '7',  '8',  '9',  '/',
    '4',  '5',  '6',  '*',
    '1',  '2',  '3',  '-',
    'C',  '0',  '=',  '+'
]

row = 1
col = 0
for key in keys:
    button = tk.Button(root, text=key, width=5, height=2, bg="lightblue")
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

display = tk.Entry(root, width=23, font=("Arial", 16))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create a separate thread to show the loading screen
loading_thread = threading.Thread(target=show_loading_screen)
loading_thread.start()

root.mainloop()
