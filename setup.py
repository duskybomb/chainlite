from setuptools import find_packages, setup

setup(
    name="chainlite",
    version="0.2.3",
    author="Sina Semnani",
    author_email="sinaj@cs.stanford.edu",
    description="A Python package that uses LangChain and LiteLLM to call large language model APIs easily",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/stanford-oval/chainlite",
    packages=find_packages(),
    install_requires=[
        "tqdm",
        "langchain",  # newer versions (up to 0.2.23) cause an error when caching is used
        "langchain-community",
        "langchain-core",
        "langchain-text-splitters",
        "langgraph",
        "langsmith",
        "litellm",
        "pydantic>=2.5",
        "redis[hiredis]",
    ],
    extras_require={
        "dev": [
            "invoke",
            "pytest",
            "pytest-asyncio",
            "setuptools",
            "wheel",
            "twine",
            "isort",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    license="Apache License 2.0",
)
