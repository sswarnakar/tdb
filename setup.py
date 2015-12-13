from setuptools import setup, find_packages

setup(
  name = 'tdb',
  packages = find_packages(),
  version = '0.1',
  description = 'TensorFlow Debugger',
  author = 'Eric Jang',
  author_email = 'ericjang2004@gmail.com',
  url = 'https://github.com/ericjang/tdb', # use the URL to the github repo
  download_url = 'https://github.com/ericjang/tdb/archive/0.1.tar.gz',
  keywords = ['Deep Learning', 'TensorFlow',  'debugging', 'visualization'], 
  classifiers = [],
  license='Apache 2.0',
  install_requires=['toposort>=1.4']
)
