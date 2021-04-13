from setuptools import setup

setup(name='Cathumbnailer',
      version='0.2',
      description='pynq-jupyter',
      url='https://mygit.th-deg.de/vt16684/cathumbnailer',
      author='vipin',
      author_email='vipin.thomas@stud.th-deg.de',
      license='MIT',
      packages=['bs4','requests','re'],
      install_requires=[
          'markdown',
      ],
      zip_safe=False)
