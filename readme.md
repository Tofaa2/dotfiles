My personal arch linux dotfiles

If you would like to use all or any of these dotfiles


1) Clone this repository somewhere safe (as the process without copying the directories requires symlinking) `git clone --depth 1 https://github.com/Tofaa2/dotfiles.git`
2) Enter the directory `cd dotfiles`

Now it splits apart.
If you want to copy over the configs for a specific application, go into the dir with  the name of the application and copy over the .config or other directories, and put them into your home folder (example: nvim/.config/nvim <-> ~/.config/nvim)

If you want to symlink setup stow with the script setup.sh and then stow [application] so if you want to symlink nvim, do stow nvim in the dotfiles directory.
The script also has an opt in install and stow everything that is made for my own use
