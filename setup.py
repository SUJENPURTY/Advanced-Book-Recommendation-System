from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

#####
REPO_NAME = "ML Based Advanced Books Recommender System"
AUTHOR_USER_NAME = "SUJEN PURTY"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="SUJEN PURTY",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SUJENPURTY/Advanced-Book-Recommendation-System.git",
    author_email="sujenpurty4@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)