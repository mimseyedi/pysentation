"""
██████╗ ██╗   ██╗███████╗███████╗███╗   ██╗████████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝ ███████╗█████╗  ██╔██╗ ██║   ██║   ███████║   ██║   ██║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝  ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
██║        ██║   ███████║███████╗██║ ╚████║   ██║   ██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

pysentation Github repository: https://github.com/mimseyedi/pysentation
"""


from setuptools import setup, find_packages
from pathlib import Path


README = Path(Path(__file__).parent, "README.md").read_text()
REQUIREMENTS = Path(Path(__file__).parent, "requirements.txt").read_text().splitlines()
exec(open('pysentation/_version.py').read())


setup (
    name = 'pysentation',
    description = 'pysentation is a CLI for displaying Python presentations.',
    version = __version__,
    packages = find_packages(),
    install_requires = REQUIREMENTS,
    python_requires='>=3.11',
    entry_points='''
        [console_scripts]
        pysentation=pysentation.pysentation:main
    ''',
    author=__author__,
    keyword=[
        "pysentation",
        "presentation",
        "CLI",
        "Python",
        "slideshow",
        "slide",
        "screen",
        "teaching",
        "education",
        "visual",
        "terminal",
    ],
    long_description=README,
    long_description_content_type="text/markdown",
    license='GNU General Public License v3 (GPLv3)',
    url='https://github.com/mimseyedi/pysentation',
    dependency_links=REQUIREMENTS,
    author_email=__email__,
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ]
)