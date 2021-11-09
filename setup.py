import os
import io

import setuptools

setuptools.setup(name='pytest-progress',
      version='1.2.3',
      description='pytest plugin for instant test progress status',
      long_description=io.open('README.rst', encoding='utf-8', errors='ignore').read(),
      author='santosh',
      author_email=u'santosh.srikanta@gmail.com',
      url=u'https://github.com/ssrikanta/pytest-progress',
      license = 'MIT',
      license_file = 'LICENSE',
      py_modules=['pytest_progress'],
      entry_points={'pytest': ['progress = pytest_progress']},
      install_requires=['pytest>=3.7'],
      packages=setuptools.find_packages(),
      keywords='py.test pytest report',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Pytest',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Testing',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
      ]
      )

