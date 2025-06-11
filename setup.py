from setuptools import setup

setup(
    name='hwifipt',
    version='1.0',
    packages=['hwifipt'],
    entry_points={
        'console_scripts': [
            'hwifipt = hwifipt.__main__:main',
        ],
    },
)
