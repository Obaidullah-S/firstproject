from setuptools import setup, find_packages

setup(
    name="obaidullah-database-automation",
    version="0.0.4",
    author="Obaidullah Stanikzai",
    packages=find_packages(),
    install_requires=[
        "pymongo",
        "pandas",
        "openpyxl"
    ],
)