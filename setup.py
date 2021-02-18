from setuptools import setup

with open('jokes/__init__.py', encoding='utf-8') as fid:
    for line in fid:
        if line.startswith('__version__'):
            VERSION = line.strip().split()[-1][1:-1]
            break

setup(
    name='LearningPlayground',
    version=VERSION,
    description='Training repo for new users to make mistakes',
    url='git@github.com:wpklab/training.git',
    author='Davis J. McGregor',
    author_email='davisjm2@illinois.edu',
    license='MIT',
    packages=['learning'],
    zip_safe=False
)
