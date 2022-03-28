import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="num_to_rus",
    version="1.0.0",
    author="Artemowkin",
    author_email="artyom.groshev2017@gmail.com",
    description="Небольшая библиотека для перевода чисел в слова русского языка",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/artemowkin/num_to_rus",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.7",
)
