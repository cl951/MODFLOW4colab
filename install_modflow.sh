# Check if MODFLOW is already installed
if ! test -f "//usr/local/bin/mf2005"; then
	echo "Installing MODFLOW and FloPy"
    wget --backups=1  https://github.com/cl951/MODFLOW4colab/raw/main/MODFLOW4colab.zip
	unzip -q -o MODFLOW4colab.zip -d /content/mfbinaries/
	chmod -R +x /content/mfbinaries
	cp -a /content/mfbinaries/. /usr/local/bin/
	pip install flopy
else
	echo "MODFLOW and FloPy already installed"
fi