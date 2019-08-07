from setuptools import setup, find_packages


setup(
    name='sphinx-qiime2-theme',
    version='0.0.1',
    license='BSD-3-Clause',
    url='https://qiime2.org',
    packages=find_packages(),
    entry_points={
        'sphinx.html_themes': [
            'qiime2 = sphinx_qiime2_theme',
        ]
    },
    package_data={
        '': ['theme.conf'],
    },
)
