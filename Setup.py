from setuptools import setup, find_packages

setup(name='logger',
 
      version='0.1',
      
      author='Andrey Popov and Nikolay Kukhalski',

      author_email='kng_by@mail.ru',
 
      url='https://github.com/nikolay-kukhalski/log_learn',
 
      license='MIT',
  
      description='Logging of training metrics',
 
      packages=find_packages(),

      install_requires= ['tensorboard>=2.0.0'],

      python_requires='>=3.8')