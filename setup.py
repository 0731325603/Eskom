from setuptools import setup, find_packages

setup(
    name='predicttools',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Package containing 7 functions for eskom predict',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/IvenoCarolus/Group5_Analyse_Predict',
    author='Iveno',
    author_email='bubblesortguru@gmail.com'
)
