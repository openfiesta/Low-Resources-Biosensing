from setuptools import setup

setup(name='lrbs_mutation_analysis',
    version='0.1',
    description='Functions for performing the described mutation analysis',
    url='https://github.com/openfiesta/Low-Resources-Biosensing/tree/master/Useful%20Scripts/Mutation%20Analysis',
    author='Francisco Javier Quero',
    author_email='franxi2953@gmail.com',
    license='MIT',
    install_requires=[
        'numpy',
        'IPython',
        'matplotlib',
        'Bio'
    ],
    packages=['lrbs_mutation_analysis'],
    zip_safe=False)