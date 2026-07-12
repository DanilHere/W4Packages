import subprocess

clear_aw = subprocess.run(["clear"], check=True)
print(clear_aw.stdout)

logo = r"""
 _    _    ___   ___  _       _            
| |  | |  /   | / _ \| |     (_)           
| |  | | / /| |/ /_\ \ |_ __  _ _ __   ___ 
| |/\| |/ /_| ||  _  | | '_ \| | '_ \ / _ \
\  /\  /\___  || | | | | |_) | | | | |  __/
 \/  \/     |_/\_| |_/_| .__/|_|_| |_|\___|
                       | |                 
                       |_|                 

A simple package manager for Alpine Linux. (Apk BTW)
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

def update_now():
    print("========UPDATE========")
    results = subprocess.run(["sudo", "apk", "update", "&&", "sudo", "apk", "upgrade"], check=True)
    
    print(results.stdout)
    print("Update complete")

def install_now():
    apps = input("packages name? ")
    print("========INSTALL========")
    print(apps)
    install_now = subprocess.run(["sudo", "apk", "add", apps], check=True)

    print(install_now.stdout)

def uninstall_now():
    apps_remove = input("packages name? ")
    print("========UNINSTALL========")
    print(apps_remove)
    uninstall_now = subprocess.run(["sudo", "apk", "del", apps_remove], check=True)

    print(uninstall_now.stdout)

def list_pack():
    list_pack = subprocess.run(["sudo", "apk", "list", "--installed"], check=True)

def search_now():
    search = input("packages name? ")
    print("========SEARCHING FOR========")
    print(search)
    search_now = subprocess.run(["sudo", "apk", "search", "-V" search], check=True)

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