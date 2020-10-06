import os
import io

from setuptools import setup


def get_version(filename):

    here = os.path.dirname(os.path.abspath(__file__))
    f = open(os.path.join(here, filename))
    version_match = f.read()
    f.close()

    if version_match:
        return version_match
    raise RuntimeError("Unable to find version string.")



setup(name='pytest-progress',
      version=get_version('version.txt'),
      description='pytest plugin for instant test progress status',
      long_description=io.open('README.rst', encoding='utf-8', errors='ignore').read(),
      author='santosh',
      author_email=u'santosh.srikanta@gmail.com',
      url=u'https://github.com/ssrikanta/pytest-progress',
      license = 'MIT',
      license_file = 'LICENSE',
      py_modules=['pytest_progress'],
      entry_points={'pytest11': ['progress = pytest_progress']},
      install_requires=['pytest>=2.7'],
      keywords='py.test pytest report',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Pytest',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Testing',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
      ]
      )

