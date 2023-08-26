"""
Script: Windows Security Measures

Description:
This script demonstrates interaction with the Windows Registry to perform system-level modifications and implements security measures on a Windows system including blocking USB ports,
disabling Bluetooth, blocking access to a specific website, and restricting the command prompt.

Author: [G Mahananda Reddy]

Usage:
    1. Run this script with administrative privileges.
    2. Test this script on a Windows 10 virtual machine.

Important Note:
    - This script modifies the Windows Registry, which can have unintended consequences if not used responsibly.
    - Test this script in a controlled environment, such as a virtual machine, where you can easily revert changes.
    - Make sure you understand the consequences and the implications this might have on your system's functionality.



"""
import winreg

# Disable USB ports
"""
    Disables USB ports by modifying the Windows Registry.
    
    This function modifies the 'Start' value in the Windows Registry for the USB storage service to disable it.
    
    Raises:
        Exception: If there's an error while accessing the Registry or performing modifications.
"""

def block_usb():
    
    key_path = r"SYSTEM\CurrentControlSet\Services\USBSTOR"
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, 4)  # Set Start to 4 to disable
        print("USB ports sucessfully blocked.")
    except Exception as e:
        print("Error:", e)

block_usb()

# Disable Bluetooth
"""
    Disables Bluetooth functionality by modifying the Windows Registry.
    
    This function modifies the 'Start' value in the Windows Registry for the Bluetooth service to disable it.
    
    Raises:
        Exception: If there's an error while accessing the Registry or performing modifications.
"""

def disable_bluetooth():
    key_path = r"SYSTEM\CurrentControlSet\Services\BTHPORT"
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, 4)  # Set Start to 4 to disable
        print("Bluetooth disabled sucessfully")
        print("Restart is required!")
    except Exception as e:
        print("Error:", e)

disable_bluetooth()

# Blocking website

# Simulate website blocking by modifying hosts file

website_to_block = "www.facebook.com"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# Open the hosts file and append redirection

with open(hosts_path, "a") as hosts_file:
    hosts_file.write(f"127.0.0.1 {website_to_block}\n")

print("facebook.com is blocked!")

# Disable Command_prompt
"""
    Restricts access to the command prompt by modifying the Windows Registry.
    
    This function creates a Registry key to restrict command prompt access.
    

    
    Raises:
        Exception: If there's an error while accessing the Registry or performing modifications.
"""


def restrict_command_prompt():
    key_path = r"Software\Policies\Microsoft\Windows\System"
    value_name = "DisableCMD"
    
    try:
        # Open the specified registry key
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            # Set the value to 1 to disable the command prompt
            winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, 1)
        print("Command prompt access is restricted.")
        print("Restart the Command Prompt to observe the changes")
    except Exception as e:
        print("Error:", e)

restrict_command_prompt()

"""
    After running and testing the script, the following outputs are expected:

    1. USB ports Blocking:
       - Output: "USB ports successfully blocked."
       - USB ports  will be disabled.
       
    2. Bluetooth Disabling:
       - Output: "Bluetooth disabled successfully."
       - Bluetooth functionality will be turned off, affecting wireless connectivity and peripherals.
       - Restart is required to affect this change.

    3. Website Blocking:
       - Output: "www.facebook.com is blocked!"
       - Attempts to access "www.facebook.com" , as the website is blocked, you'll see a connection error or the browser will fail to load the page.

    4. Command Prompt Restriction:
       - Output: "Command prompt access is restricted."
       - Restart the command prompt to observe the changes.
       - Command prompt access will be restricted, preventing its usage.
       - After running the script, try opening the Command Prompt by typing "cmd" in the Start menu or pressing Win + R and entering "cmd".
       - You should receive a message stating that access to the Command Prompt has been restricted by the system administrator.

"""








