from setuptools import setup

with open('learning/__init__.py', encoding='utf-8') as fid:
    for line in fid:
        if line.startswith('__version__'):
            VERSION = line.strip().split()[-1][1:-1]
            break

setup(
    name='TrainingTutorials',
    version=VERSION,
    description='Training repo designed for practicing and making mistakes',
    url='git@github.com:djmcgregor/training.git',
    author='Davis J. McGregor',
    author_email='davisjm2@illinois.edu',
    license='MIT',
    packages=['learning'],
    zip_safe=False
)
