#!/usr/bin/env python

from distutils.core import setup, Extension
import os

with open('README.rst') as readme_file:
    readme = readme_file.read()

def mecab_config(arg):
    return os.popen("mecab-config " + arg).readlines()[0].split()

inc_dir  = mecab_config("--inc-dir")
lib_dirs = mecab_config("--libs-only-L")
libs     = mecab_config("--libs-only-l")

swig_opts = ['-shadow', '-c++']
swig_opts.extend("-I"+d for d in inc_dir)

setup(name = "mecab-python3",
    version = '0.8.1',
    description = 'python wrapper for mecab: Morphological Analysis engine',
    long_description=readme,
    maintainer = 'Tatsuro Yasukawa',
    maintainer_email = 't.yasukawa01@gmail.com',
    url = 'https://github.com/SamuraiT/mecab-python3',
    license = 'BSD',
    py_modules = ["MeCab"],
    ext_modules = [
        Extension("_MeCab",
                  ["MeCab.i"],
                  include_dirs = inc_dir,
                  library_dirs = lib_dirs,
                  libraries    = libs,
                  swig_opts    = swig_opts)
    ],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Environment :: MacOS X",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
