from setuptools import setup

setup(
    name='vsdebug',
    entry_points={
        'console_scripts': [
            'vsdebug = vsdebug:parse_input',
        ],
    }
)
