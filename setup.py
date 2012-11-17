from setuptools import setup

setup(name='BookType',
    version='1.0',
    description='BookType',
    author='Your Name',
    author_email='example@example.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=[
            'Django==1.3',
            'South==0.7.5',
            'unidecode',
            'lxml',
            'PIL',
            'redis',
        ],
    )
