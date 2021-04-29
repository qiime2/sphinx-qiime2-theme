# ----------------------------------------------------------------------------
# Copyright (c) 2019-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from os import path


def setup(app):
    app.add_html_theme('qiime2', path.abspath(path.dirname(__file__)))
