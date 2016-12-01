from setuptools import setup
from setuptools.extension import Extension

setup(
    name='round3',
    version='0.1.0',
    description='Backport of Python 3 built-in round',
    author='Cosimo Lupo',
    author_email='cosimo.lupo@daltonmaag.com',
    url='http://github.com/anthrotype/round3',
    license='Python Software Foundation License',
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License',
    ],
    ext_modules=[
        Extension("round3", sources=['round3.c'])
    ],
)
