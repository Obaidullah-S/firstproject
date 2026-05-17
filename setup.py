from setuptools import setup, find_packages

setup(
    name="obaidullah-database-automation",
    version="0.0.5",
    author="Obaidullah Stanikzai",

    package_dir={"": "src"},
    packages=find_packages(where="src"),

    install_requires=[
        "pymongo",
        "pandas",
        "openpyxl"
    ],
)