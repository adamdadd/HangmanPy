from setuptools import setup
import os


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
   name='HangmanPy',
   version='0.1.0',
   description='Terminal Hangman Game. Written in pure python.',
   license="MIT",
   long_desciption=read('README.md'),
   author='Adam Dad',
   author_email='adam-dad@hotmail.co.uk',
   url="https://github.com/adamdadd/HangmanPy",
   packages=['HangmanPy']
)
