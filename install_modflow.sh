# Install MODFLOW binaries for cl961
wget --backups=1  https://github.com/cl951/MODFLOW4colab/raw/main/MODFLOW4colab.zip
unzip -q -o MODFLOW4colab.zip -d /content/mfbinaries/
chmod -R +x /content/mfbinaries
cp -a /content/mfbinaries/. /usr/local/bin/	
