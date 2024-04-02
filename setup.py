from setuptools import setup, find_packages

setup(
    name='Query2DataFrame',
    version='0.1.0',
    author='Shashank Goud',
    author_email='shashaankgoud@gmail.com',
    description=('From SQL queries to pandas DataFrames: Query2DataFrame makes it easy to retrieve, '
                 'aggregate, and save data from PostgreSQL, enhancing data analysis and machine learning projects.'),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Shazankk/Query2DataFrame',
    packages=find_packages(),
    py_modules=['data_toolkit'],
    install_requires=[
        'pandas>=1.2.0',
        'psycopg2-binary>=2.8.6',
        'openpyxl>=3.0.5',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
