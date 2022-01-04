from setuptools import setup, find_packages
# Follows https://www.youtube.com/watch?v=zhpI6Yhz9_4

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science',
    'License :: OSI Approved :: GPL v3 License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
]

setup(
    name='thesis_data_readers',
    version='0.0.1',
    author="Olusanmi Hundogan",
    author_email="o.hundogan@gmail.com",
    description='A reader package for specific logs within process mining',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/Olu93/thesis_data_readers',
    project_urls={
        "Bug Tracker": "https://github.com/Olu93/thesis_data_readers/issues",
    },
    classifiers=classifiers,
    package_dir={"": "src"},

    packages=find_packages(where="src"),
    install_requires=open('requirements.txt').read().split('\n'),
    python_requires='>=3.6',
    keywords="reader, xes, log, BPIC",
)
