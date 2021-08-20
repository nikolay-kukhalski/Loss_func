from setuptools import setup, find_packages


def open_require(path_file):
    with open(path_file, "r") as f_list:
        add_requires = f_list.readlines()
    return [line.rstrip('\n') for line in add_requires]


setup(
    name='logger_metric',
    version='0.1',
    author='Andrei Papou and Nikolay Kukhalski',
    author_email='kng_by@mail.ru',
    url='https://github.com/nikolay-kukhalski/logger_metric',
    license='MIT',
    description='Logging of training metrics',
    packages=find_packages(),
    extras_require={
        'tblog': open_require('requirements/tblog.txt'),
        'tfcallback': open_require('requirements/tfcallback.txt')
    },
    python_requires='>=3.8'
    )
