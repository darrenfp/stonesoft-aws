from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='stonesoft-aws',
      version='0.2.17',
      description='Stonesoft NGFW deployer for AWS',
      url='http://github.com/gabstopper/stonesoft-aws',
      author='David LePage',
      author_email='dwlepage70@gmail.com',
      license='Apache 2.0',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
	    'smc-python>=0.5.5',
        'boto3',
        'ipaddress',
        'pyyaml'
      ],
      entry_points={
        'console_scripts': [
                'ngfw_launcher=deploy.__main__:main'
        ]
      },
      classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: System :: Networking :: Firewalls",
        ],
      zip_safe=False)
