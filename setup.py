from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='qspace',
    version='0.0.7',
    packages=find_packages(where='src'),  # Specify src directory
    package_dir={'': 'src'},  # Define the root package directory
    install_requires=[
        'twine',
        'setuptools',
        'wheel',
        'flake8',
        'black',
        'pytest',
        'pip-upgrader',
        'asyncclick',
        'azure-quantum',
        'qsharp',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'qspace=q:cli',  # Update to point to q.cli
        ],
    },
    author='rUv',
    description='Q-Space, a cutting-edge deployment wizard designed to simplify the process of setting up and managing quantum computing applications using Azure Quantum and Azure Functions.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
