from setuptools import setup

REQUIREMENTS = []
with open("requirements.txt", "r") as f:
    REQUIREMENTS = f.read().splitlines()

README = ""
with open("README.md", "r") as f:
    README = f.read()

setup(
    name="AoC-helper",
    version="2023.12.01",
    description="A small AoC helper package",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/isaa-ctaylor/aoc-helper",
    author="isaa_ctaylor",
    author_email="isaac@isaactaylor.xyz",
    license="GPL-3.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=["aoc_helper"],
    include_package_data=True,
    install_requires=REQUIREMENTS,
)