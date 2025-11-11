import os
import io

from setuptools import setup


def get_version(filename):
    """Get version from version file."""
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, filename), 'r', encoding='utf-8') as f:
        version_match = f.read().strip()
    
    if version_match:
        return version_match
    raise RuntimeError("Unable to find version string.")



setup(name='pytest-progress',
      version=get_version('version.txt'),
      description='pytest plugin for instant test progress status',
      long_description=io.open('README.rst', encoding='utf-8').read(),
      author='santosh',
      author_email=u'santosh.srikanta@gmail.com',
      url=u'https://github.com/ssrikanta/pytest-progress',
      license='MIT',
      license_files=['LICENSE'],
      packages=['pytest_progress'],
      entry_points={'pytest11': ['progress = pytest_progress']},
      install_requires=['pytest>=2.7'],
      python_requires='>=3.8',
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
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12',

      ]
      )

