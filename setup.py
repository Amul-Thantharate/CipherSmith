from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="passforge",
    version="0.1.0",
    author_email="amulthantharate@gmail.com",
    author="Amul Thantharate",
    description="A powerful and flexible command-line password generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Amul-Thantharate/passforge",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Topic :: Utilities",
    ],
    python_requires=">=3.9",
    install_requires=[
        "typer[all]>=0.9.0",
        "colorama>=0.4.6",
        "cryptography>=41.0.0",
        "pyyaml>=6.0.1",
    ],
    entry_points={
        "console_scripts": [
            "passforge=app.main:main",
        ],
    },
    include_package_data=True,
    keywords="password generator cli security cryptography",
    project_urls={
        "Bug Tracker": "https://github.com/Amul-Thantharate/passforge/issues",
        "Documentation": "https://passforge.readthedocs.io",
        "Source Code": "https://github.com/Amul-Thantharate/passforge",
    },
)
