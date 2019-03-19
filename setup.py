from setuptools import setup, find_packages

setup(
    name='Hello',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/siphe2009/Hello',
    author='<Siphesihle Yapi>',
    author_email='<siphe2009@gmail.com>'
)
