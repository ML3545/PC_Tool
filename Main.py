import tkinter
import tkinter as tk
from tkinter import ttk
from downloads import *
from win_settings import *

def create_GUI():
    root = tk.Tk()
    root.title("MEIR PC Tool")
    # root.geometry('600x600')
    # frm = ttk.Frame(root)
    # frm.pack(padx=10, pady=10)
    # frm.grid()
    downloads(root)
    # settings(frm)
    root.mainloop()


def downloads(root):
    #Downloads
    var = tk.IntVar()
    # cb_chrome = ttk.Checkbutton(frm, text="Chrome", variable=var).grid(column=0, row=0, padx=10, pady=3)
    # cb_vlc = ttk.Checkbutton(frm, text="VLC Pleyar").grid(column=0, row=1, padx=10, pady=3)
    checkboxes = {}
    checkbox_var = {}

    # Create checkboxes
    packages = ["Chrome", "VLC Player"]  # Add your package names here
    for package_name in packages:
        var = tk.IntVar(value=0)
        checkbox_var[package_name] = var
        checkbox = tk.Checkbutton(root, text=package_name, variable=var)
        checkboxes[checkbox] = package_name
        checkbox.pack(anchor=tk.W)

    btn_install = ttk.Button(root, text="Install", command=download_click(var)).pack()


# def settings():
#     #Settings
#     cb_storageSense = ttk.Checkbutton(frm, text="Srorage Sense").grid(column=1, row=0, padx=10, pady=3)
#     btn_enable_settings = ttk.Button(frm, text="Enable Settings").grid(column=1, row=2, padx=10, pady=3)


def main():
    create_GUI()
    # install_chrome()
    # install_vlc()

if __name__ == "__main__":
    main()
