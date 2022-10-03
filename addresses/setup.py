# Table setup
from setuptools import setup
from os import path

# directory containing the file
file_dir = path.abspath(path.dirname(__file__))
with open(path.join(file_dir,'README.md'),encoding ='utf-8') as f:
    description =f.read()

setup(
    name = 'addresses',
    version = '0.1.1',
    author = 'Muhoza Ursus Bizumuremyi',
    install_requires = ['numpy', 'pandas',
                        'pandas_datareader',
                        'datetime',
                        'beautifulsoup4',
                        'geojson',
                        'lxml',
                        'matplotlib',
                        'ujson',
                        'xarray',
                        'pyspark'
                        ],

    extra_require ={'test':['pytest','pytest-sugar']},
    keywords = ['addresses','address','idjwi','OpenStreetMap','OSM'],
    license='MIT',
    classifiers=[
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
		"Operating System :: OS Independent"]

)
