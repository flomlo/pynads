import os
from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from distutils.version import LooseVersion
from pybind11.setup_helpers import Pybind11Extension, build_ext

with open('pynads/_version.py', 'r') as f:
    exec(f.read())

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

nads_bindings_builder = Pybind11Extension("pynads/nads_bind", ['src/nads_bindings.cpp'],
        extra_compile_args = ['-std=c++14', '-DMANY_VERTICES'])


setup(
    name="pynads", 
    version=__version__,
    author="Florian Unger",
    author_email="florian.unger@posteo.net",
    license='GPLv3',
    description="Python bindings to `nads`, a C++ number-of-almost-d-simplices computer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flomlo/pynads",
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        'Programming Language :: C++',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
    install_requires=['numpy >= 1.17.0', 'setuptools', 'pybind11 >= 2.6.0'],
    ext_modules=[nads_bindings_builder],
    include_package_data=True
)
