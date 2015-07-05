try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Steve Gledhill',
    'url': 'URL to get it at',
    'downloard_url': 'Where to download it',
    'author_email': 'steve@pcresolver.es',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)