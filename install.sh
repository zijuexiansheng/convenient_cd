#!/bin/bash

if [[ "$#" -ne "1" ]]; then
    echo "Usage: ./install.sh <install path>"
    exit
fi

curdir=$PWD

rm -rf $1
mkdir -p $1/bin
mkdir -p $1/libexec/bin
mkdir -p $1/libexec/completions/zsh
mkdir -p $1/var/ccd/
cd $1
install_dir=$PWD
cd ${curdir}

cp ${curdir}/src/ccd ${install_dir}/bin/
cp ${curdir}/src/ccd_loader.zsh ${install_dir}/bin/
cp ${curdir}/src/pyccd.py ${install_dir}/libexec/bin/
cp ${curdir}/src/_ccd ${install_dir}/libexec/completions/zsh
sed -i.bak 's#=>replace me<=#'"${install_dir}/libexec/bin/pyccd.py"'#' ${install_dir}/bin/ccd
sed -i.bak 's#=>replace me<=#'"${install_dir}"'#' ${install_dir}/bin/ccd_loader.zsh
sed -i.bak 's#=>replace me<=#'"${install_dir}/var/ccd/ccd.db"'#' ${install_dir}/libexec/bin/pyccd.py
sed -i.bak 's#=>replace me<=#'"${install_dir}/libexec/bin/pyccd.py"'#' ${install_dir}/libexec/completions/zsh/_ccd
rm ${install_dir}/bin/ccd.bak
rm ${install_dir}/bin/ccd_loader.zsh.bak
rm ${install_dir}/libexec/bin/pyccd.py.bak
rm ${install_dir}/libexec/completions/zsh/_ccd.bak
python2 ${install_dir}/libexec/bin/pyccd.py create

echo "'ccd' command has been installed to [${install_dir}/bin]"
echo "To use this command, add the following to your ~/.zshrc"
echo "    source ${install_dir}/lib/bin/ccd_loader.zsh"
