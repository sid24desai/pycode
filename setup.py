from setuptools import setup, find_packages

setup(
    name='pycode',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn'
    ],
    entry_points={
        'console_scripts': [
            'pycode=pycode.cli:main'
        ]
    }
)
