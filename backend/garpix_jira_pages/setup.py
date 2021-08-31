from setuptools import setup, find_packages
from os import path
from m2r import convert
from django.conf import settings


with open(path.join(settings.BASE_DIR, '..', 'README.md'), encoding='utf-8') as f:
    long_description = convert(f.read())

setup(
    name='garpix_jira_pages',
    version='1.1.0',
    description='',
    long_description=long_description,
    url='https://github.com/garpixcms/garpix_jira',
    author='Garpix LTD',
    author_email='info@garpix.com',
    license='MIT',
    packages=find_packages(exclude=['testproject', 'testproject.*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'garpixcms >= 2.0.2',
        'garpix_jira >= 1.1.0',
    ],
)

