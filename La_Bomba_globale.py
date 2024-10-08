import tkinter as tk
from tkinter import messagebox

def show_warning():
    answer = messagebox.askyesno("Internet Connection Wizard", "sei sicuro di volore eseguire?\n")
    if answer:
        print("Hai cliccato si")
    else:
        print("Hai cliccato No")


root = tk.Tk()
root.withdraw()  
show_warning()
root.quit()


def show_warning():
    messagebox.showwarning("Internet Connection Wizard", "vuoi eseguire")
    print("Hai cliccato OK")
root = tk.Tk()
root.withdraw()  
show_warning()
root.quit()
