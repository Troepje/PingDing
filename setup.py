from setuptools import setup

setup(name='PingDing',
      version='0.0.0',
      description='Graphically show ping result of various nodes',
      author='Troepje',
      author_email='',
      url='https://github.com/Troepje/PingDing',
      packages=['PingDing'],
      package_dir={'PingDing':  'src/'},
      install_requires=[
          'argparse'
      ],
      entry_points={
           'console_scripts': [
               'PingDing = PingDing:main'
           ]
      }
    )
