Title: Installing ASE and GPAW in Anaconda 3
Date: 2019-09-03 14:29
Category: Post
Author: Fadjar Fathurrahman

In this post, I will describe how to install [ASE](https://wiki.fysik.dtu.dk/ase/) and
[GPAW](https://wiki.fysik.dtu.dk/gpaw/) in an Anaconda 3 Linux distribution.

Remember to active the Anaconda 3 environment first.

```
source activate /opt/anaconda3/bin/activate
```

(assuming that your Anaconda 3 distribution is installed at `/opt/anaconda3`)


# Installing ASE

## Install the requirements:
  
According to [the manual](https://wiki.fysik.dtu.dk/ase/install.html) the requirements are:
  
Mandotory:
- Python 3.5 or newer
- NumPy 1.10 or newer (base N-dimensional array package)
- SciPy 0.16 or newer (library for scientific computing)
  
Optional:
- Matplotlib 2.0.0 or newer (plotting)
- tkinter (for ase.gui)
- Flask (for ase.db web-interface)
  
Standard Anaconda 3 (not Miniconda) distribution should already have these requirements.

## Download and unpack the distribution tarball.

```
tar xvf ase-3.18.1.tar.gz
cd ase-3.18.1
python setup.py build
python setup.py install
```

Please change the version number accordingly.

For the last step (`python setup.py install`), you might need administrator access.



# Installing GNU compilers and build tools for Anaconda 3

```
conda install gcc_linux64 gfortran_linux64 autotools
```

Install MPI:
```
conda install -c conda-forge openmpi
```

This is required to build Libxc and binary dependecies of GPAW.


# Installing Libxc

Download and unpack the tarball.

Configuring LibXC (after change directory to topdir of Libxc)
```
cd build
cmake -D CMAKE_INSTALL_PREFIX=/opt/anaconda3/ ../
make -j 4 # use 4 cores
```

# Installing GPAW

```
# LibXC:
# In order to link libxc installed in a non-standard location
# (e.g.: configure --prefix=/home/user/libxc-2.0.1-1), use:

# - static linking:
if 1:
    xc = '/opt/anaconda3/'
    include_dirs += [xc + 'include']
    extra_link_args += [xc + 'lib64/libxc.a']
    if 'xc' in libraries:
        libraries.remove('xc')
```

Build
```
python setup.py build
python setup.py install
```
