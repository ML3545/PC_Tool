import subprocess

def install_chrome():
    # Command to install Chrome with Winget
    command = ["winget", "install", "-e", "--id", "Google.Chrome"]

    # Execute the command
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def install_vlc():
    # Command to install vlc with Winget
    command = ["winget", "install", "-e", "--force", "--id", "VideoLAN.VLC"]

    # Execute the command
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


# checkbox value
def print_checkbox_status(checkboxes, checkbox_var):
    for checkbox, package_name in checkboxes.items():
        if checkbox_var[package_name].get() == 1:
            if checkbox_var[package_name]:
                install_chrome()
            else:
                install_vlc()
        else:
            print(f"{package_name} is not selected")