from setuptools import setup, find_packages

with open("requirements/logger.txt", "r") as f_logger:
	logger_txt = f_logger.readlines()
logger_txt = [line.rstrip('\n') for line in logger_txt]


with open("requirements/tf.txt", "r") as f_tf:
	tf_txt = f_tf.readlines()
tf_txt = [line.rstrip('\n') for line in tf_txt]



setup(name='logger',
 
      version='0.1',

      author='Andrei Papou and Nikolay Kukhalski',

      author_email='kng_by@mail.ru',
 
      url='https://github.com/nikolay-kukhalski/log_learn',
 
      license='MIT',
  
      description='Logging of training metrics',
 
      packages=find_packages(),

      extras_require={'TB': logger_txt, 'TF': tf_txt},

      #install_requires= ['tensorboard>=2.0.0'],

      python_requires='>=3.8')