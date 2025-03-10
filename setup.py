from setuptools import setup, find_packages

setup(
    name="expense_tracker",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'python-dateutil>=2.8',
        'argparse>=1.4'
    ],
    entry_points={
        'console_scripts': [
            'expense-tracker=expense_tracker.cli:main'
        ],
    },
)