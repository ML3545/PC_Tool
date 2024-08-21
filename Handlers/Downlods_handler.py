import subprocess

# check software list
def check_software_installed(software_name):
    command = f"Get-WmiObject -Query \"SELECT * FROM Win32_Product WHERE Name='{software_name}'\""
    result = subprocess.run(command)
    if software_name in result.stdout:
        print(f"{software_name} is installed.")
    else:
        print(f"{software_name} is not installed.")

    # PowerShell command to search for the specific software package
    # command = f'powershell.exe Get-Package -Name "*{software_name}*"'
    # process = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # output, error = process.communicate()
    #
    # # Print the output
    # print("Output:\n", output.decode())
    # print("Error:\n", error.decode())

    # command = f'wmic product where "name like \'%{software_name}%\'" get name'
    # output = subprocess.run(command)
    # print(output)
    # if output.returncode != 0:
    #     print(software_name)
    # return False

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