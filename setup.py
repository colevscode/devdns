import os
from distutils.core import setup

root = os.path.dirname(os.path.realpath(__file__))

setup(
    name='devdns',
    version='0.1.0',
    author='Cole Krumbholz',
    author_email='cole@brace.io',
    description='A DNS server for mapping a dev TLD to localhost.',
    packages=['devdns'],
    long_description=open(root+"/README.md").read(),
    license='LICENSE',
)