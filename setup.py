from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="CipherSmith",
    version="1.3.0",
    author="Amul Thantharate",
    author_email="amulthantharate@gmail.com",
    description="A powerful password generator with real-time strength analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amulthantharate/CipherSmith",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "typer>=0.9.0",
        "rich>=10.0.0",
        "zxcvbn-python>=4.4.24",
        "cryptography>=41.0.0",
        "sqlalchemy>=2.0.0",
        "click>=8.0.0",
        "colorama>=0.4.4",
    ],
    entry_points={
        "console_scripts": [
            "CipherSmith=app.main:app",
        ],
    },
    include_package_data=True,
)
