import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
# file_path = filedialog.askopenfilename()
file_path = filedialog.askdirectory()

print(file_path)