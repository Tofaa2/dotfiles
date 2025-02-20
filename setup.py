import os
import shutil


import os
import shutil

def copyOver(directory, destination):
    directory = os.path.expanduser(directory)
    destination = os.path.expanduser(destination)
    print(f"Copying files from {directory} to {destination}")

    if not os.path.exists(directory):
        print(f"Source directory {directory} does not exist. Skipping...")
        return

    if os.path.isdir(directory):
        if not os.path.exists(destination):
            print(f"Creating destination directory: {destination}")
            os.makedirs(destination)
        
        for root, dirs, files in os.walk(directory):
            for fname in files:
                src = os.path.join(root, fname)
                dst = os.path.join(destination, os.path.relpath(src, directory))
                dst_dir = os.path.dirname(dst)

                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)

                shutil.copy2(src, dst)
    else:
        shutil.copy2(directory, destination)

def copyOverConf(file):
    copyOver('.config/' + file + '/', '~/.config/' + file)

def printScarryWarning():
    input("THIS SCRIPT IS PURELY FOR MY OWN CONVENIENCE AND WILL SYMLINK INSTEAD OF DIRECTLY WRITING TO THE CONFIG LOCATIONS. IF YOU DONT WANT TO DO THAT THEN JUST MANUALLY COPY PASTE IDK? Press any key to continue")

def installPackages(packages):
    value = input(f'Attempting to install packages {", ".join(packages)} Y/N? ').lower()
    if value == 'n':
        print("Skipping package install")
    elif value == 'y':
        print("Installing packages...")
        os.system("sudo pacman -Sy " + " ".join(packages))
    else:
        print(f'Invalid input, expected Y/N got {value} Skipping package install...')


if __name__ == '__main__':
    printScarryWarning()
    installPackages(["ghostty", "neovim", "firefox", "fastfetch"])
   
    copyOverConf('nvim')
    copyOverConf('hypr')
    copyOverConf('fastfetch')
    copyOverConf('wofi')
    #copyOver('.config/nvim/', '~/.config/nvim')
    #copyOver('.config/fastfetch', '~/.config/fastfetch')

