from setuptools import setup, find_packages

def open_require(path_file = None):
      with open(path_file, "r") as f_list:
	      add_requires = f_list.readlines()
      return [line.rstrip('\n') for line in add_requires]



setup(name='logger',
 
      version='0.1',

      author='Andrei Papou and Nikolay Kukhalski',

      author_email='kng_by@mail.ru',
 
      url='https://github.com/nikolay-kukhalski/log_learn',
 
      license='MIT',
  
      description='Logging of training metrics',
 
      packages=find_packages(),

      extras_require={'TB': open_require('requirements/logger.txt'), 'TF': open_require('requirements/tf.txt')},

      #install_requires= ['tensorboard>=2.0.0'],

      python_requires='>=3.8')