# ----------------------------------------------------------------------------
# Copyright (c) 2019-2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

project = 'Demo Documentation'
copyright = '2020, q2d2'
author = 'q2d2'
extensions = []
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'qiime2'
html_static_path = ['_static']
html_theme_options = {
    'navbar_resource_urls': {
        'Dev Docs': 'https://dev.qiime2.org/',
        'Docs': 'https://docs.qiime2.org/',
        'Forum': 'https://forum.qiime2.org/',
        'Library': 'https://library.qiime2.org/',
        'Main Site': 'https://qiime2.org/',
        'View': 'https://view.qiime2.org/',
        'Workshops': 'https://workshops.qiime2.org/',
    },
}
