from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

if __name__ == "__main__":

    setup(
        name='eunomia',
        description='Install the configuration files for different linters and formatter in an specific project',
        author='Mohammed Boujemaoui Boulaghmoudi',
        author_email='mohabouje@gmail.com',
        license='MIT',
        license_files='LICENSE',
        url='https://github.com/mohabouje/eunomia',
        version='0.0.1.beta',
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'eunomia = eunomia.__main__:main'
            ],
        },
        include_package_data=True,
        zip_safe=False,
        install_reqs=required,
        python_requires='>=3.6',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
        ],
    )
