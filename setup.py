from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
        name='VMData',
        version='1.0',
        description='Extract metadata from video.',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/lappanchappan43/VMdata",
        packages=['VMData'],
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
        zip_safe=False,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.5',
    )

