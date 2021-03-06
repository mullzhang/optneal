import os
from setuptools import setup, find_packages


def read_requirements():
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


description = 'Python library for mathematical optimization using annealing and LP solvers.'

setup(
    name='optneal',
    version='0.0.7',
    description=description, long_description='README.md',
    author='Mull Zhang',
    install_requires=['dimod', 'numpy'],
    url='https://github.com/mullzhang/optneal',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)
