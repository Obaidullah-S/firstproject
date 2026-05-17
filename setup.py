from setuptools import setup, find_packages

setup(
    name="obaidullah-database-automation",
    version="0.0.9",
    author="Obaidullah Stanikzai",

    package_dir={"": "src"},
    packages=find_packages(where="src"),
    py_modules=["database_automation"],

    install_requires=[
        "pymongo",
        "pandas",
        "openpyxl"
    ],
)