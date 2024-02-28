import subprocess
from Main import *


def install_chrome():
    # Command to install Chrome with Winget
    command = ["winget", "install", "--id", "Google.Chrome"]

    # Execute the command
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def install_vlc():
    # Command to install vlc with Winget
    command = ["winget", "install", "-e", "VLC media player"]

    # Execute the command
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


# checkbox value
def print_checkbox_status(checkboxes, checkbox_var):
    for checkbox, package_name in checkboxes.items():
        if checkbox_var[package_name].get() == 1:
            print(f"{package_name} is selected")
        else:
            print(f"{package_name} is not selected")
