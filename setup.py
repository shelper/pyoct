#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # use packages in the requirements.txt
]

test_requirements = [
    'pytest',
]

setup(
    name='pypeline',
    version='0.1.0',
    description="python based packages for Optical Coherence Tomography applications",
    long_description=readme + '\n\n' + history,
    author="Zhijia Yuan",
    author_email='shelpermisc@gmail.com',
    url='https://github.com/shelper/pypeline',
    packages=[
        'pypeline',
    ],
    package_dir={'pypeline':
                 'pypeline'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='pypeline',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
