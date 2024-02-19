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


def download_click(v):
    if v.get() == 1:
        print("Yes")