from setuptools import setup

setup(name='pytplinkrouter',
      version='0.1.0',
      description='Access TPLink routers',
      url='http://github.com/ericpignet/pytplinkrouter',
      author='Eric Pignet',
      author_email='eric@erixpage.com',
      license='MIT',
      install_requires=['requests>=2.0'],
      packages=['pytplinkrouter'],
      zip_safe=True)
