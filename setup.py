from setuptools import setup, find_packages

setup(
    name='preferably',
    version=0.1,
    author='Alex Peitsinis',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'preferably = preferably.indicator:main'
        ]
    },
    include_package_data=True,
    zip_safe=False
)
