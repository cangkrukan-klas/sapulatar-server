import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sapulatarserver",
    version="0.0.1",
    description="Sapulatar backend web service for online use",
    author="Fadhil Yori Hibatullah",
    author_email="me@fadhilyori.my.id",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devlovers-id/sapulatar-server",
    project_urls={
        "Bug Tracker": "https://github.com/devlovers-id/sapulatar-server/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Framework :: Flask"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        'flask>=2.0.0',
        'Pillow>=8.2.0',
        'rembg>=1.0.25'
    ],
    setup_requires=[
        'flake8>=3.9.0',
        'pytest-runner>=5.3.0',
        'setuptools>=44.0.0'
    ]
)
