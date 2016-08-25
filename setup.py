from setuptools import setup, find_packages

setup(
    name='indicator_scripts',
    version=0.1,
    author='Alex Peitsinis',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'indicator-scripts = indicator_scripts.indicator:main'
        ]
    },
    include_package_data=True,
    zip_safe=False
)
