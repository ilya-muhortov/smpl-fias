import setuptools
from os.path import join, dirname

import smpl_fias

setuptools.setup(
    name='smpl-fias',
    packages=setuptools.find_packages(),
    version=smpl_fias.__version__,
    license='MIT',
    url='https://github.com/ilya-muhortov/smpl-fias',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type="text/markdown"
)
