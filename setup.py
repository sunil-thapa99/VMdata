from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
        name='VMdata',
        version='1.0',
        description='Extract metadata from video.',
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=['VMdata'],
        author='Sunil Thapa',
        author_email='sunil43thapa@gmail.com',
        install_requires=['future'],
        extras_require={
            'dev': [
                'future',
                'numpy',
                'opencv-python',
            ]
        },
        zip_safe=False
    )

