from setuptools import setup, find_packages

setup(
    name="expense_tracker",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'expense-tracker=expense_tracker.cli:main',
        ],
    },
)