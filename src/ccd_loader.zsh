#!/usr/bin/env zsh

autoload -Uz "=>replace me<=/bin/ccd"
fpath=(=>replace me<=/libexec/completions/zsh $fpath)
autoload -U compinit
compinit
