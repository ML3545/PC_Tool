import tkinter as tk
from tkinter.constants import DISABLED

from Handlers.Downlods_handler import print_checkbox_status, check_software_installed
from Handlers.win_settings_handler import apply_settings

checkboxes = {}
checkbox_var = {}


def create_GUI():
    root = tk.Tk()
    root.title("MEIR PC Tool")
    downloads(root)
    settings(root)
    root.geometry('300x300')
    root.mainloop()
    # frm = ttk.Frame(root)
    # frm.pack(padx=10, pady=10)
    # frm.grid()
    # downloads(root)
    # settings(frm)

def downloads(root):
    # cb_chrome = ttk.Checkbutton(frm, text="Chrome", variable=var).grid(column=0, row=0, padx=10, pady=3)
    # cb_vlc = ttk.Checkbutton(frm, text="VLC Pleyar").grid(column=0, row=1, padx=10, pady=3)

    # Create checkboxes
    packages = ["Google Chrome", "VLC Media Player", "Firefox"]  # Add your package names here
    for package_name in packages:
        var = tk.IntVar(value=0)
        checkbox_var[package_name] = var
        checkbox = tk.Checkbutton(root, text=package_name, variable=var)
        checkboxes[checkbox] = package_name
        checkbox.pack(anchor=tk.W)
        result = check_software_installed(package_name)
        print(result)
        if result != 0:
            checkbox.config(state=DISABLED)


    btn_install = tk.Button(root, text="Install", command=lambda: print_checkbox_status(checkboxes, checkbox_var))
    btn_install.pack()


def settings(root):
    btn_enable_settings = tk.Button(root, text="Enable Settings", command=apply_settings)
    btn_enable_settings.pack()


def main():
    create_GUI()


if __name__ == "__main__":
    main()
