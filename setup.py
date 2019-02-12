from setuptools import setup, find_packages

setup(
    name='gj_union',
    version='v0.1.0',
    description='SDB query backend',
    author='Jonas Sølvsteen',
    author_email='josl@dhigroup.com',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'flask',
        'shapely[vectorized]',
        'geojson'
    ],
    extras_require={
        'deploy': [
            'awscli',
            'zappa'
        ],
        'test': [
            'pytest',
            'codecov',
            'pytest-cov',
            'pytest-flake8'
        ]
    }
)
