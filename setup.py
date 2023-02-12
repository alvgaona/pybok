from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pybok',
    version='0.0.1',
    author='Alvaro Gaona',
    author_email='alvgaona@gmail.com',
    description='A brief description of pybok',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/username/pybok',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
