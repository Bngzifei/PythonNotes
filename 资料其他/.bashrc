# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# xycloud style alias
if [ x"$UID" = x"0" ]; then
    PS1='\[\033[01;31m\]\h:\[\033[01;34m\]\w \[\033[00m\]\[\033[01;31m\]#\[\033[00m\]'
else
    PS1='\[\033[01;31m\]\u@\h:\[\033[01;34m\]\w \[\033[00m\]\[\033[01;31m\]$\[\033[00m\]'
fi
alias ls="ls -F --color=auto"
alias l="ls"
alias ll="ls -l"
alias la="ls -A"
alias lsd="ls -d */"
alias lh="ls -lAh"
alias s="cd .."
alias p="cd -"
alias md="mkdir"
alias rd="rmdir"
alias rm="rm -i"
alias cp="cp -i"
alias mv="mv -i"
alias x="exit"
alias h="history"
alias du="du -h"
alias df="df -h"
alias free="free -m"
INPUTRC=/etc/inputrc
export PS1 INPUTRC
[ x"$TERM" = x"linux" ] && setfont lat9u-16 >/dev/null 2>&1