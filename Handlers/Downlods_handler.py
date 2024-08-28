import subprocess

# check software list
def check_software_installed(software_name):
    command = f'powershell.exe Get-Package -Name "*{software_name}*"'
    process = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    process.communicate()
    print(process.returncode)
    return process.returncode

# install a software with Winget
def install_software(software_name):
    print(software_name)
    command = ["winget", "install", "-e", "--id", f"{software_name}"]

    # Execute the command
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# checkbox value
def print_checkbox_status (checkboxes, checkbox_var):
    software_names = ["Google.Chrome", "VideoLAN.VLC"]
    for index, package_name in zip(software_names, checkboxes.values()):
        if checkbox_var[package_name].get() == 1:
                install_software(index)
        else:
            print("Please select")