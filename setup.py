from setuptools import setup, find_packages

setup(
    name="unlimited_machine_translator",
    version="1.1.0",
    description="A package for unlimited machine translation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Axel-Vs/unlimited_machine_translator",
    packages=find_packages(),
    install_requires=[
        "deep_translator",
        "pandas",
        "numpy",
        "nltk",
        "python-docx",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
)
