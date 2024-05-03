from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
print(here)
setup(name='PingDing',
      version='0.0.0',
      description='Graphically show ping result of various nodes',
      author='Bob',
      author_email='',
      url='',
      packages=['PingDing'],
      package_dir={'PingDing':  '%s/src/' % here},
      install_requires=[
          'subprocess',
          'tkinter',
          'argparse'
      ]
     )
