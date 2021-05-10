import re

from setuptools import setup, find_packages
from os import path

HERE = path.abspath(path.dirname(__file__))


def readfile(*parts):
    with open(path.join(HERE, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = readfile(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M,
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string')


setup(
    name='JenkinsLauncher',
    version=find_version('src', 'JenkinsLauncher', '__init__.py'),
    description='Jenkins Job launcher',
    url='https://github.com/rukavishnikovmihail00/JenkinsLauncher',
    author='Mikhail Rukavishnikov',
    author_email='rukavishnikovmihail00@yandex.ru',
    license='Proprietary License',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Operating System :: POSIX :: Linux'
    ],
    packages=find_packages(where='src', include=('JenkinsLauncher*',)),
    package_dir={'JenkinsLauncher': '/'},
    python_requires='>=3.7',
    install_requires=[
        'pyyaml>=5.3.1',
        'jenkinsapi==0.3.11',
        'Jinja2==2.11.3',
    ],
    package_data={
        'JenkinsLauncher': ['templates/']
    },
    entry_points={
        'console_scripts': [
            'JenkinsLauncher = JenkinsLauncher.start:main'
        ]
    }
)
