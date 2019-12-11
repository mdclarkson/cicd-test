import setuptools
from cicd_test import __version__ as version

name = 'cicd-test'
description = 'CICD pipeline tests'
keywords = []

install_requires = [
]

author = 'Chuck Orde'
author_email = 'chuckorde@gmail.com'
repo = 'https://github.com/chuckorde'

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
        name = name,
        packages = setuptools.find_packages(),
        version = version,
        license = 'MIT',
        description = description,
        long_description=long_description,
        long_description_content_type='text/markdown',
        author = author,
        author_email = author_email,
        url = repo + '/' name,
        download_url = url + '/archive/v' + version + '.tar.gz',
        keywords = keywords,
        install_requires = install_requires,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
         ],
        python_requires=' >= 3.5',
)

