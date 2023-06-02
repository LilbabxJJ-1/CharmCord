import setuptools
with open("README.md", "r") as rd:
    longtext = rd.read()

setuptools.setup(
    # Here is the module name.
    name="AoiPy",
    version="0.11.3",
    author="Jade",
    description="Aoi.py is the best python string-based package for Discord bot devs",
    long_description=longtext,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),

    # if module has dependencies i.e. if your package rely on other package at pypi.org
    # then you must add there, in order to download every requirement of package
    install_requires=["Py-cord", "Discord"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)