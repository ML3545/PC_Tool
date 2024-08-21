import subprocess

# check software list
def check_software_installed(software_name):
    command = f'powershell.exe Get-Package -Name "*{software_name}*"'
    process = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    process.communicate()
    return process.returncode


# chrome
def install_chrome():
    # Command to install Chrome with Winget
    command = ["winget", "install", "-e", "--id", "Google.Chrome"]

    # Execute the command
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# vlc
def install_vlc():
    # Command to install vlc with Winget
    command = ["winget", "install", "-e", "--id", "VideoLAN.VLC"]

    # Execute the command
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# checkbox value
def print_checkbox_status (checkboxes, checkbox_var):
    for checkbox, package_name in checkboxes.items():
        if checkbox_var[package_name].get() == 1:
            if str(checkbox_var[package_name]) == "PY_VAR0":
                install_chrome()
            elif str(checkbox_var[package_name]) == "PY_VAR1":
                install_vlc()
        else:
            print("Please select")