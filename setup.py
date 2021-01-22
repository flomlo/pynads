from setuptools import setup, Extension, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

nads_module = Extension('nads',
        sources = ['src/nads_binding.cpp'])

setup(
    name="pynads", 
    version="0.1.0",
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
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
    install_requires=['numpy >= 1.17.0'],
    ext_modules = [nads_module]
)
