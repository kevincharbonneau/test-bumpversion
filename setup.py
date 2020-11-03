"""
`setup.py` for the test-bumpversion.

This library is a fake library to test features offered by `bump2version` lib.
"""

from setuptools import Command, find_packages, setup

with open('VERSION', 'r') as version_file:
    version = version_file.read().strip()

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

setups = ['setuptools']
install = ['pandas==1.1.2']

# Add dependencies required for the new module 
# in the `extras` variable.
extras = {
    'ci': ['twine', 'bump2version'],
}

setup(name='test-bumpversion',
    version=version,
    description='\
        This is a fake library to test bump2version features',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Kevin Charbonneau',
    author_email=[''],
    url='https://github.com/kevincharbonneau/test-bumpversion',
    packages=find_packages(where='src'),
    package_dir={ '': 'src' },
    keywords=['test', 'bumpversion'],
    python_requires='>=3.6',
    setup_requires=setups,
    install_requires=install,
    extras_require=extras
)
