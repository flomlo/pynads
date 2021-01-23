from setuptools import setup, Extension, find_packages

with open('pynads/_version.py', 'r') as f:
    exec(f.read())

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

#nads_module = Extension('nads',
#        include_dirs=[os.path.join(this_dir, 'include')],
#        sources=[os.path.join(this_dir, 'src', 'nads_binding.cpp')]

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
    install_requires=['numpy >= 1.17.0'],
#    ext_modules = [nads_module],
    include_package_data=True
)
