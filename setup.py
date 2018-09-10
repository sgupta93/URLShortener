import codecs
from os import path
from setuptools import setup, find_packages

with open('requirements.txt') as reqs:
    install_requires = [line for line in reqs.read().split('\n') if (
        line and not line.startswith('--'))
    ]

def read(*parts):
    return codecs.open(path.join(path.dirname(__file__), *parts),
                       encoding="utf-8").read()

setup(name='url_shortener',
      version='1.0.0',
      description='URL Shortener Web Based Application',
      long_description=read('README.rst'),
      url='https://github.com/sgupta93/URLShortener.git',
      author='Shital Gupta(50536)',
      author_email='shital.gupta@aricent.com',
      license='ARICENT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      scripts=['bin/url-shortener'],
      classifiers=[
          'Development Status :: 1 - Development',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: ARICENT License',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.7.0'
      ],
      zip_safe=False)
