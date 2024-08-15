import subprocess

def apply_settings():
    # storage sense
    # PowerShell command to enable Storage Sense
    ps_command = """
    $key_storage = "HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\StorageSense\\Parameters\\StoragePolicy"
    $key_update = "HKLM:\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings"
    
    If (!(Test-Path $key_storage -and $key_update)) {
        New-Item -Path $key -Force | Out-Null
    }
    Set-ItemProperty -Path $key_storage -Name "01" -Value 1 -Type DWord -Force
    Set-ItemProperty -Path $key_storage -Name "2048" -Value 30 -Type DWord -Force # Set for 30 Days 
    Set-ItemProperty -Path $key_update -Name "IsContinuousInnovationOptedIn" -Value 1 -Type DWord -Force   # enable get the latest update...  
    Set-ItemProperty -Path $key_update -Name "IsExpedited" -Value 1 -Type DWord -Force    # enable get me up to date 
    
    """

    # Run the PowerShell command
    command = ["powershell.exe", "-Command", ps_command]
    result = subprocess.run(command, capture_output=True, text=True)

    return
