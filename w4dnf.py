import subprocess

clear_aw = subprocess.run(["clear"], check=True)
print(clear_aw.stdout)

logo = r"""
 _    _    _________        __ 
| |  | |  /   |  _  \      / _|
| |  | | / /| | | | |_ __ | |_ 
| |/\| |/ /_| | | | | '_ \|  _|
\  /\  /\___  | |/ /| | | | |  
 \/  \/     |_/___/ |_| |_|_|  

A simple package manager for Fedora. (Dnf BTW)
"""
 # user interfaces
interfaces = r"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                                                          MAIN MENU                                                                   $
$                                                                                                                                      $
$    (U)Update          (I)Install          (X)Uninstall    (C)Clear cache      (L)List All Packages     (S)Search                     $
$                                                                                                                                      $
$                                                                                                                                      $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""
print(logo)
print(interfaces)

# Main Function 
def update_now():
    print("========UPDATE========")
    results = subprocess.run(["sudo", "dnf", "check-update", "&&", "sudo", "dnf", "upgrade"], check=True)
    
    print(results.stdout)
    print("Update complete")

def install_now():
    apps = input("packages name? ")
    print("========INSTALL========")
    print(apps)
    install_now = subprocess.run(["sudo", "dnf", "install", apps], check=True)

    print(install_now.stdout)

def uninstall_now():
    apps_remove = input("packages name? ")
    print("========UNINSTALL========")
    print(apps_remove)
    uninstall_now = subprocess.run(["sudo", "dnf", "remove", apps_remove], check=True)

    print(uninstall_now.stdout)

def list_pack():
    list_pack = subprocess.run(["sudo", "dnf", "list", "installed"], check=True)

def search_now():
    search = input("packages name? ")
    print("========SEARCHING FOR========")
    print(search)
    search_now = subprocess.run(["dnf", "search", search], check=True)

# User Input
print("Type q then press enter for exit")
mode = input(">>> ")
print(mode)


if mode == "U":
    update_now()

elif mode == "I":
    install_now()

elif mode == "X":
    uninstall_now()

elif mode == "L":
    list_pack()

elif mode == "S":
    search_now()


else:
    print("exit")