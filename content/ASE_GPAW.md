Title: Installing ASE and GPAW in Anaconda 3
Date: 2019-09-03 14:29
Category: Post

Activate Anaconda environment first.



Installing ASE



Libxc-4.3.4

Configuring LibXC:
```
cmake -D CMAKE_INSTALL_PREFIX=/home/efefer/miniconda3/ ../
make -j 4
```

GPAW
```
# LibXC:
# In order to link libxc installed in a non-standard location
# (e.g.: configure --prefix=/home/user/libxc-2.0.1-1), use:

# - static linking:
if 1:
    xc = '/home/efefer/miniconda3/'
    include_dirs += [xc + 'include']
    extra_link_args += [xc + 'lib64/libxc.a']
    if 'xc' in libraries:
        libraries.remove('xc')
```

