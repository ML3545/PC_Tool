import tkinter as tk
from downloads import *

def create_GUI():
    root = tk.Tk()
    root.title("MEIR PC Tool")
    # root.geometry('600x600')
    # frm = ttk.Frame(root)
    # frm.pack(padx=10, pady=10)
    # frm.grid()
    # downloads(root)
    # settings(frm)
    return root


def downloads(root):
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

    btn_install = tk.Button(root, text="Install", command=print_checkbox_status(checkboxes, checkbox_var))
    btn_install.pack()


# def settings():
#     #Settings
#     cb_storageSense = ttk.Checkbutton(frm, text="Storage Sense").grid(column=1, row=0, padx=10, pady=3)
#     btn_enable_settings = ttk.Button(frm, text="Enable Settings").grid(column=1, row=2, padx=10, pady=3)


def main():
    root = create_GUI()
    downloads(root)
    # install_chrome()
    # install_vlc()
    root.mainloop()


if __name__ == "__main__":
    main()
