from setuptools import setup, find_packages

setup(
    name="ETL-SQL-drktao",
    version="0.0.1",
    description="ETL with local SQL database",
    install_requires=["click==8.1.3","colorama"],
    entry_points="""
    [console_scripts]
    etl-package=main:main
    """,
    author="Derek Tao",
    author_email="derek.tao@duke.edu",
    packages=find_packages(),
)