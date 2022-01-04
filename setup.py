from setuptools import setup, find_packages
# Follows https://www.youtube.com/watch?v=zhpI6Yhz9_4

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science',
    'License :: OSI Approved :: GPL v3 License',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python :: 3'
]

setup(
    name='BPICLogReaders',
    version='0.0.1',
    description='A reader package for specific logs within process mining',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    url='',
    classifiers = classifiers,
    packages = find_packages(),
    install_requires=open('requirements.txt').read().split('\n'),
    author="Olusanmi Hundogan",
    author_email="o.hundogan@gmail.com",
    license="GPL", 
    keywords="reader, xes, log, BPIC"
)