from distutils.core import setup
import sys

import maemogcalsync as mgs

setup(name=mgs.__name__,
      version=mgs.__version__,
      author=mgs.__author__,
      author_email=mgs.__author_email__,
      url=mgs.__url__,
      description=mgs.__doc__.split("\n")[0],
      long_description=pysafe.__doc__,
      packages=['maemogcalsync'],
      provides=['maemogcalsync'],
      license='LGPL v3'
)
