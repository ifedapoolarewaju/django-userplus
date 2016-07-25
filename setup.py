from setuptools import setup

setup(name='django-userplus',
      version='0.2',
      description='Extended Auth User module for Django',
      url='https://github.com/ifedapoolarewaju/django-userplus.git',
      author='Ifedapo Olarewaju',
      author_email='ifedapoolarewaju@gmail.com',
      license='MIT',
      packages=['userplus', 'userplus.lib'],
      install_requires=['Django>=1.8', 'Django<1.10'],
      zip_safe=False)
