from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
print(here)
setup(name='PingDing',
      version='0.0.0',
      description='Graphically show ping result of various nodes',
      author='Troepje',
      author_email='',
      url='https://github.com/Troepje/PingDing',
      packages=['PingDing'],
      package_dir={'PingDing':  '%s/src/' % here},
      install_requires=[
          'argparse'
      ],
      entry_points={
           'console_scripts': [
               'PingDing = PingDing:main'
           ]
      }
    )
