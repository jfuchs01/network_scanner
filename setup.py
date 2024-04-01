from setuptools import setup, find_packages

setup(
    name='AdvancedNetworkScanner',
    version='1.0.0',
    author='Jordan Fuchs',
    author_email='jordan@example.com',
    description='A comprehensive network scanning tool with GUI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jfuchs01/advanced-network-scanner',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyQt5',
        'scapy',
        'python-nmap'
    ],
    entry_points={
        'gui_scripts': [
            'advanced-network-scanner=gui.main_window:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities'
    ],
    python_requires='>=3.6',
)
