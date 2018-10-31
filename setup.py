from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

try:
    # Get the long description from the relevant file
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''

setup(
    name='walletobjects',
    version='0.0.0',
    description='Helper Library for Google Pay Passes / Walletobjects',
    long_description=long_description,
    url='https://github.com/pc-coholic/python-walletobjects',
    author='Martin Gross',
    author_email='martin@pc-coholic.de',
    license='GNU Lesser General Public License v3 (LGPLv3)',
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(include=['walletobjects', 'walletobjects.*']),
)
