""" solitaire
"""

from setuptools import setup, find_packages

setup(
    name='solitaire',
    version='1.0',
    url='https://github.com/sinner-/solitaire',
    author='Sina Sadeghi',
    description='Python implementation of Solitaire cipher from Cryptonomicon',
    packages=find_packages(),
    install_requires=['Click>=6.7'],
    entry_points={
        'console_scripts': [
            'solitaire = solitaire.cmd.cli:main',
        ]},
)
