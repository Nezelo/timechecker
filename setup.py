from setuptools import setup, find_packages

setup(
    name="timecheckerza",
    version="0.0.2",
    author="Bongani Mondlane",
    author_email="proneezy@hotmail.com",
    url="",
    description="An application that informs you of the time in different locations and timezones nje",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["timechecker = src.main:main"]},
)
