from setuptools import setup

with open("README.md") as f:
    readme = f.read()

setup(
    name="tkvideo-moviepy",
    version="0.1.0",
    description="Play moviepy video clips with tkiner",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Multimedia :: Video :: Display",
    ],
    keywords="tkvideo tkinter video display label pillow imageio huskee moviepy",
    url="https://github.com/MysteryBlokHed/tkvideo-moviepy",
    author="Adam Thompson-Sharpe",
    author_email="adamthompsonsharpe@gmail.com",
    license="MIT",
    packages=["tkvideo"],
    install_requires=["moviepy", "Pillow"],
    include_package_data=True,
    zip_safe=False,
)
