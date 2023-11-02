from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Project Planner'
LONG_DESCRIPTION = 'Small app for planning projects or tasks with option to seperate larger tasks into smaller steps'

setup(
    name="Project planner",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Krzysztof Jaszewski",
    license='MIT',
    packages=find_packages(),
    install_requires=['colorama','keyboard'],
    keywords=['planner'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ],
    entry_points={'console_scripts':['RunPlanner = Planner.planner:main']}
)
