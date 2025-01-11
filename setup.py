import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()
    
    
__version__ = "0.0.0"

REPO_NAME = "Text_Summarizer"
AUTHOR_USER_NAME = "Vaibhav rai"
AUTHOR_EMAIL = "vairaibhav922@gmail.com"
Src_repo = "text_summarization"

setuptools.setup(
    name=Src_repo,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/VaibhavRai24/Text-Summarizer",
    project_urls={
        "Bug Tracker" : f"https://github.com/VaibhavRai24/Text-Summarizer",},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
    