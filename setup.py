import os
import sys

from pip.req import parse_requirements
from setuptools import setup
from setuptools.command.test import test as TestCommand

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open("README.md", 'r') as readme_file:
    readme = readme_file.read()

install_reqs = parse_requirements('requirements.txt')
requirements = [str(ir.req) for ir in install_reqs if ir.req is not None]

setup(
    name='glowstick',
    version='0.1',
    author='Ryan Senkbeil',
    author_email='me@ryansenkbeil.com',
    description='HDHomerun...',
    long_description=readme,
    packages=['glowstick'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=requirements,
    scripts=["bin/glowstick"],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    tests_require=['tox'],
    cmdclass ={'test': Tox},
)
