from setuptools import setup, find_packages

setup(
    name="finguard-ai",
    version="1.0.0",
    packages=find_packages(include=["apps*", "backend*", "packages*", "ml*", "pipelines*"]),
    include_package_data=True,
    python_requires=">=3.10",
)
