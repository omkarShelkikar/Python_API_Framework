from setuptools import setup, find_packages

setup(
    name="Python_API_Framework",
    version="1.0.0",
    description="A Python-based API framework for development and testing.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "flask==2.3.2",
        "requests==2.31.0",
        "pytest==7.4.2",
        "pytest-flask==1.2.0",
        "python-dotenv==1.0.0",
    ],
)