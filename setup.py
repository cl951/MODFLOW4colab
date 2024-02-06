import os
import platform
import subprocess
import pkg_resources
from setuptools import find_packages, setup

setup(
    name="MODFLOW4colab",
    py_modules=["MODFLOW4colab"],
    version="0.1",
    description="Install selected MODFLOW binaries into Google FloPy for use with FloPy. N.B. Selected MODFLOW ARM binaries only, only including those relevant to class CL951 taught at University of Strathclyde",
    readme="README.md",
    python_requires=">=3.8",
    author="Yannick Kremer",
    url="https://github.com/cl951/MODFLOW4colab",
    license=""
)



# Check if the file does not exist
if not os.path.isfile("/usr/local/bin/mf2005"):
    # Download the file using wget
    #subprocess.run(["wget", "--backups=1", "http://personal.strath.ac.uk/yannick.kremer/CL951/colab_install/mfbinariescl951.zip"])
    
    # Unzip the downloaded file quietly and overwrite files without prompting
    #subprocess.run(["unzip", "-q", "-o", "mfbinariescl951.zip", "-d", "/content/mfbinaries/"])
    
    # Change the mode of files to executable recursively
    subprocess.run(["chmod", "-R", "+x", "/content/mfbinaries"])
    
    # Copy all files from source to destination
    subprocess.run(["cp", "-a", "/content/mfbinaries/.", "/usr/local/bin/"])
    
    # Install the flopy package using pip
    subprocess.run(["pip", "install", "flopy"])