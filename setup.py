from setuptools import setup, find_packages
from pathlib import Path

# Requirements
try:
    this_directory = Path(__file__).absolute().parent
    with open((this_directory / "requirements.txt"), encoding="utf-8") as f:
        requirements = f.readlines()
    requirements = [line.strip() for line in requirements]
except FileNotFoundError:
    requirements = []

# Metadata
setup(
    name="treepy",
    version="0",
    author="stho",
    author_email="q@q",
    description="Describe here your package in one sentence",
    license="Type here what license your package has",
    packages=find_packages(),
    install_requires=requirements
)
