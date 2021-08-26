from setuptools import setup

setup(
   name='simple_thread',
   version='0.1',
   author='Malte Iwanicki',
   author_email='malteiwa@gmail.com',
   packages=['simple_thread', 'simple_thread.test'],
   description='A simple way to start a function in a thread',
   long_description=open('README.txt').read(),
   install_requires=[
       "pytest"
   ],
)