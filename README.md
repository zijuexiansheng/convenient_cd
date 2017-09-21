# convenient_cd

A convenient cd command. This tool works best with your the Zsh completion. So please follow the instructions to load the Zsh completion after installing this tool!

# dependencies

* python
* zsh

# install

* `./install.sh <install path>`, or
* `brew install zijuexiansheng/filbat/convenient_cd`

# Usage

```
Usage: ccd <path_name> <extra_path> ...
   or: ccd --cmd <cmd_name>
    <cmd_name>:
         * insert <path_name> <path>:     add a path
         * delete <path_name> ...:        delete one or more paths by name
         * update <path_name> <path>:     delete one or more paths by name
         * avail:                         list available paths
         * clear:                         clear all paths
```

# Examples

Each of the following example will suppose that you are current in the `$HOME` directory and there is a directory called `$HOME/lol`

## Example 1

```
$ ccd --cmd insert lol $HOME/hehe/lol
$ ccd --cmd insert github $HOME/hehe/github
$ ccd --cmd avail
lol: /your/home/directory/hehe/lol
github: /your/home/directory/hehe/github
$ ccd --cmd delete github
$ ccd --cmd avail
lol: /your/home/directory/hehe/lol
```

### Example 2

* `ccd lol aaa/bbb ccc/ddd`, or
* `ccd lol aaa bbb ccc ddd`, or
* `ccd lol aaa/bbb/ccc/ddd`

This will change the current working directory to `$HOME/hehe/lol/aaa/bbb/ccc/ddd`

**Note**: There is no `/` after `lol`

### Example 3

* `ccd lol/ aaa bbb`, or
* `ccd lol/aaa bbb`, or
* `ccd lol/ aaa/bbb`, or
* `ccd lol/aaa/bbb`

This will change the current working directory to `$HOME/lol/aaa/bbb`

**Note** There is a `/` after `lol`

---

**Note**

1. `<path name>` should not start with `-`
2. If a `<path name>` is identical with an actually existing path, the `<path name>` will be used. In practice, it's recommended not use any `/` in a `<path name>` so that we can always differentiate it with an actual path by appending a `/` after the actual path name
