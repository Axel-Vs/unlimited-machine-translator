from setuptools import setup, find_packages

setup(
    name="unlimited_machine_translator",
    version="1.1.6",
    description="A package for perform unlimited machine translation via batches",
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
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 5 - Production/Stable",
    ],
    python_requires=">=3.6",
)
