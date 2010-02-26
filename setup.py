import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'repoze.bfg',
    'repoze.zodbconn',
    'repoze.tm',
    'repoze.folder',
    'ZODB3',
    ]

tests_require = requires.extend([
        'nose',
        ])

setup(name='rfd',
      version='0.0',
      description='rfd',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: BFG",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = requires,
      tests_require=tests_require,
      test_suite="rfd",
      entry_points = """\
      [paste.app_factory]
      app = rfd.run:app
      """
      )

