from setuptools import setup, find_packages

setup(name='logger',
 
      version='0.1',

      author='Andrei Papou and Nikolay Kukhalski',

      author_email='kng_by@mail.ru',
 
      url='https://github.com/nikolay-kukhalski/log_learn',
 
      license='MIT',
  
      description='Logging of training metrics',
 
      packages=find_packages(),

      extras_require={
        'TB': ['tensorboard>=2.4.0'], 'TF': ['tensorflow>=2.4.0'] 
    }

      #install_requires= ['tensorboard>=2.0.0'],

      python_requires='>=3.8')