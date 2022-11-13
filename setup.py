#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: Innary
@ Date: 2022-11-11 12:02:08
@ LastEditors: Innary
@ LastEditTime: 2022-11-13 02:08:40
'''
from setuptools import setup
import os
requirements = [
    'tqdm',
    'pypandoc'
    
]

init_fn = os.path.join(os.path.dirname(__file__), 'file_transform', '__init__.py')
with open(init_fn) as f:
    for l in f.readlines():
        if '__version__' in l:
            exec(l)
            break
def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content

setup(
    name='TextTransfor',
    version=__version__,
    author = 'Innary', 
    author_email = 'wyc1015128645@gmail.com',
    description='a script of text file transform',
    # long_description=readme(), 
    long_description_content_type='text/markdown',
    url='https://github.com/Innary/testtransfor',
    install_requires=requirements,
    packages=['file_transform'],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'tt = file_transform.main:main',
        ],
    },
    
)