import os
from setuptools import setup

packages = []
for d, _, _ in os.walk('load_dependencies_magic'):
    if 'venv' not in d and os.path.exists(os.path.join(d, '__init__.py')):
        packages.append(d.replace(os.path.sep, '.'))

requirements = [
    'nbformat',
    'IPython',
    'urllib3',
    'requests'
]

setup(
    name="LoadDependenciesMagic",
    version="0.0.1dev0",
    author="Nikhil Fulzele",
    author_email="nikhilf99@gmail.com",
    description="Notebook magic to load dependencies like .ipynb, .csv, .py, .txt located on remote server importable",
    license="MIT",
    packages=packages,
    install_requires=requirements
)
