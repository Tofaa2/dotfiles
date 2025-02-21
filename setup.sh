#!/bin/bash

echo "WARNING: This script will install GNU Stow for easy symlink."
echo "It will not however install any of the packages needed in these configuration files"
echo "You will have to do that yourself."
read -p "Do you want to continue? (y/n): " choice

if [[ "$choice" != "y" && "$choice" != "Y" ]]; then
    echo "Aborting setup."
    exit 1
fi

sudo pacman -Sy stow
echo "Setup completed successfully!"

echo "WARNING: Now the script will attempt to install the default software i personally use. Its essentially every application in this configuration"

read -p "Do you want to continue? (y/n): " choice2

if [["$choice2$" != "y" && "$choice2" != "Y" ]]; then
  echo "Aborting installation."
  exit 1
fi

sudo pacman -Sy waybar pavucontrol swaync ghostty neovim firefox fastfetch
stow waybar sway nvim fastfetch

echo "Completed installation"

