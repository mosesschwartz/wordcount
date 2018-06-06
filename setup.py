from setuptools import setup

setup(name='wordcount',
      version='1.0',
      description='Swagger-documented Flask-based API to count words in text.',
      url='https://github.com/mosesschwartz/wordcount',
      author='Moses Schwartz',
      author_email='moses.schwartz@gmail.com',
      license='MIT',
      packages=['wordcount'],
      install_requires=['flask', 'flask-restplus'],
      zip_safe=False)