from setuptools import setup
import src.hol004.version as ver

setup(
    include_package_data=True,
    version=ver.__version__
)