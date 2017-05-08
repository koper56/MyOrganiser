from setuptools import find_packages
from setuptools import setup


setup(
    name='morg',
    version='1.0.0',
    packages=find_packages(include=('morg*',)),
    install_requires=open('requirements.txt').read(),
    entry_points={
        'console_scripts': [
            'morg = morg:run',
        ],
    },
)
