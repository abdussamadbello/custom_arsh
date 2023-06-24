from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_arsh/__init__.py
from custom_arsh import __version__ as version

setup(
	name="custom_arsh",
	version=version,
	description="Arsh customization",
	author="optisol",
	author_email="optisol.ltd@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
