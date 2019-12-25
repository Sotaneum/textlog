from setuptools import setup, find_packages
import textlog
setup(name='textlog',
      version=textlog.__version__,
      url='https://github.com/Sotaneum/textlog',
      license='MIT',
      author='LEE DONG GUN',
      author_email='gnyotnu39@gmail.com',
      description='Simple python text log',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      zip_safe=False,
      setup_requires=[],
      classifiers=[
          'License :: OSI Approved :: MIT License'
      ]
)
