#
# ~/.bashrc
#
eval "$(starship init bash)" # Starship for pretty :3


[[ $- != *i* ]] && return

alias vi='nvim'
alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '
