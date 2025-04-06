import setuptools

__version__ = "0.0.1"

with open("README.md", "r", encoding="utf-8") as f:
    long_descriptrion = f.read()

REPO_NAME = "FSDSCNNCLASSIFIER"
AUTHOR_NAME = "Shubham Kondewar"
SRC_REPO = "CNNClasifier"
AUTHOR_Email = "shubhamkondewar98@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_NAME,
    author_email = AUTHOR_Email,
    description = "this is my classification project",
    long_description = long_descriptrion,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",

    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    } ,

    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src") 
)

