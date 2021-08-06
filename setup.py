from setuptools import setup
from setuptools import find_packages

import sys

def setup_package():
  install_requires = ['math']
  metadata = dict(
      name = 'conv_shapes',
      version = '0.0.1',
      description = 'conv_shapes: utilities for thinking about convolution shapes',
      url = 'https://github.com/jacobhepkema/conv_shapes',
      author = 'Jacob Hepkema',
      license = 'MIT License',
      packages = find_packages(),
      install_requires = install_requires
    )

  setup(**metadata)

if __name__ == '__main__':
  if sys.version_info < (2,7):
    sys.exit('Sorry, Python < 2.7 is not supported')
    
  setup_package()
