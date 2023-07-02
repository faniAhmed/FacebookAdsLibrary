"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_packages
setup(
    name="FacebookAdsLibrary",
    author="Farhan Ahmed",
    author_email="jattfarhan10@gmail.com",
    url="https://github.com/faniAhmed/FacebookAdsLibrary",
    description="A scraper for getting Ads from Facebook Ads Library",
    version="1.0.0",
    packages=find_packages(),
    download_url= '',
    keywords= ['Facebook', 'Library', 'Transparency', 'Scraper', 'API', 'Ads', 'Facebook Ads', 'Ads Library', 'Facebook Library', 'Facebook Transparency', 'Facebook Transparency Scraper', 'Facebook Ads Library', 'Facebook Ads Scraper'],
    license='Securely Incorporation',
    install_requires=[
        "setuptools>=45.0",
        "Requests>=2.31.0",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: Free for non-commercial use",
        "Natural Language :: Urdu",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    platforms=["any"],
)