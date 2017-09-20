#!/usr/bin/env zsh

fpath=(=>replace me<=/libexec/completions/zsh =>replace me<=/bin $fpath)
autoload -Uz ccd
autoload -U compinit
compinit
