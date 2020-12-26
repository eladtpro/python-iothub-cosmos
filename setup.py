import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eladtal",
    version="1.0.1",
    author="Elad Tal",
    author_email="eladt.pro@gmail.com",
    description="Python Azure IoT Hub event client and subscriber with events stored in Cosmos DB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eladtpro/python-iothub-cosmos",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
