import subprocess

def apply_settings():
    # storage sense
    # PowerShell command to enable Storage Sense
    ps_command = """
    $key = "HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\StorageSense\\Parameters\\StoragePolicy"
    If (!(Test-Path $key)) {
        New-Item -Path $key -Force | Out-Null
    }
    Set-ItemProperty -Path $key -Name "01" -Value 1 -Type DWord -Force
    Set-ItemProperty -Path $key -Name "2048" -Value 30 -Type DWord -Force # Set for 30 Days 
    """

    # Run the PowerShell command
    command = ["powershell.exe", "-Command", ps_command]
    result = subprocess.run(command, capture_output=True, text=True)

    return
