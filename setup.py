import setuptools

with open("README.md", "r") as rd:
    longtext = rd.read()

setuptools.setup(
    # Here is the module name.
    name="CharmCord",
    version="0.18.11",
    author="Jade",
    description="CharmCord is the best python string-based package for Discord bot devs",
    long_description=longtext,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    # if module has dependencies i.e. if your package rely on other package at pypi.org
    # then you must add there, in order to download every requirement of package
    install_requires=["discord.py", "pytz"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
