from setuptools import setup, find_packages

setup(
    name='criteo-performance-downloader',
    version='1.0.0',

    description="Downloads data from the Criteo API to local files",

    install_requires=[
        'click>=6.0',
        'pycriteo<=0.0.2'
    ],

    dependency_links=[
        'https://github.com/fdellavedova/pycriteo/archive/373609b47976fc3f637f053c9f14575158ee843a.zip#egg=pycriteo-0.0.2'],

    packages=find_packages(),

    author='Mara contributors',
    license='MIT',

    entry_points={
        'console_scripts': [
            'download-criteo-performance-data=criteo_downloader.cli:download_data'
        ]
    }
)
