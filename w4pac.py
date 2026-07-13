import subprocess

clear_aw = subprocess.run(["clear"], check=True)
print(clear_aw.stdout)

logo = r"""
 _    _    ___ ______                                
| |  | |  /   || ___ \                               
| |  | | / /| || |_/ /_ _  ___ _ __ ___   __ _ _ __  
| |/\| |/ /_| ||  __/ _` |/ __| '_ ` _ \ / _` | '_ \ 
\  /\  /\___  || | | (_| | (__| | | | | | (_| | | | |
 \/  \/     |_/\_|  \__,_|\___|_| |_| |_|\__,_|_| |_|

       A simple package manager for Arch Linux. (Pacman BTW)
"""
 # user interfaces
interfaces = r"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                                                          MAIN MENU                                                                   $
$                                                                                                                                      $
$    (U)Update          (I)Install          (X)Uninstall[including config & junk files]      (L)List All Packages     (S)Search        $
$                                                                                                                                      $
$                                                                                                                                      $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""
print(logo)
print(interfaces)

# Main Function 
def update_now():
    print("========UPDATE========")
    results = subprocess.run(["sudo", "pacman", "-Syu"], check=True)
    
    print(results.stdout)
    print("Update complete")

def install_now():
    apps = input("packages name? ")
    print("========INSTALL========")
    print(apps)
    install_now = subprocess.run(["sudo", "pacman", "-S", apps], check=True)

    print(install_now.stdout)

def uninstall_now():
    apps_remove = input("packages name? ")
    print("========UNINSTALL========")
    print(apps_remove)
    uninstall_now = subprocess.run(["sudo", "pacman", "-Rns", apps_remove], check=True)

    print(uninstall_now.stdout)

def list_pack():
    list_pack = subprocess.run(["pacman", "-Q"], check=True)

def search_now():
    search = input("packages name? ")
    print("========SEARCHING FOR========")
    print(search)
    search_now = subprocess.run(["pacman", "-Ss", search], check=True)


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