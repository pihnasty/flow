from setuptools import setup, find_packages

setup(
    name='flow',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        "common_utils @ git+https://github.com/pihnasty/common_utils.git@main",
    ],
    url='http://example.com',
    license='MIT',
    author='Oleh',
    author_email='pihnastyi@gmail.com',
    description='analytics and report'
)
