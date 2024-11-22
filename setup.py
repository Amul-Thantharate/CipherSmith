from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="CipherSmith",
    version="1.3.0",
    author="Amul Thantharate",
    author_email="amulthantharate@gmail.com",
    description="A powerful and secure password management tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amulthantharate/CipherSmith",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Security :: Cryptography",
        "Topic :: Security",
    ],
    python_requires=">=3.9",
    install_requires=[
        "cryptography>=41.0.0",
        "typer>=0.9.0",
        "rich>=10.0.0",
        "zxcvbn-python>=4.4.24",
        "sqlalchemy>=2.0.0",
        "click>=8.0.0",
        "colorama>=0.4.4",
    ],
    extras_require={
        'dev': [
            'black>=23.0.0',
            'flake8>=6.0.0',
            'isort>=5.0.0',
        ],
    },
    entry_points={
        "console_scripts": [
            "ciphersmith=ciphersmith.cli:main",
        ],
    },
    include_package_data=True,
)
