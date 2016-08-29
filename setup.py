from setuptools import setup

setup(name='django-userplus',
      version='0.3',
      description='Extended Auth User module for Django',
      url='https://github.com/ifedapoolarewaju/django-userplus.git',
      author='Ifedapo Olarewaju',
      author_email='ifedapoolarewaju@gmail.com',
      license='MIT',
      packages=['userplus', 'userplus.lib'],
      install_requires=['Django>=1.9'],
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Framework :: Django'
      ],
      zip_safe=False)
