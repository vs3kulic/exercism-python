from setuptools import setup, find_packages

# Read the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="grainsy",  # Name of your library
    version="1.0.2",  # Increment version number
    description="Library for calculating grains on a chessboard",
    long_description=long_description,  # Include README.md content
    long_description_content_type="text/markdown",  # Specify Markdown format
    author="Vajo Sekulic",
    author_email="hello@bekindstudio.at",
    packages=find_packages(),  # Automatically find packages
    include_package_data=True,  # Include non-code files like README.md
    install_requires=[],  # List dependencies if any
    python_requires=">=3.11",  # Minimum Python version
)