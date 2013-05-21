# -*- coding: utf-8 -*-
#
# This file is part of VilfredoReloadedCore.
#
# Copyright (c) 2013 Daniele Pizzolli <daniele@ahref.eu>
#
# VilfredoReloadedCore is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation version 3 of the License.
#
# VilfredoReloadedCore is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License
# for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with VilfredoReloadedCore.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################


"""
Vilfredo Reloaded Core
======================

:copyright: (c) 2013 by Daniele Pizzolli
:license: AGPL 3, see LICENSE.txt for more details


Module documentation
--------------------

.. automodule:: VilfredoReloadedCore.defaults_settings
  :members:

.. automodule:: VilfredoReloadedCore.database
  :members:

.. automodule:: VilfredoReloadedCore.models
  :members:

.. automodule:: VilfredoReloadedCore.views
  :members:

.. automodule:: VilfredoReloadedCore.main
  :members:
"""

import pkg_resources
pkg_resources.declare_namespace(__name__)


# The __init__.py must contain the app
# http://flask.pocoo.org/docs/patterns/packages/
# but the __init__.py is run by setup.py
# http://stackoverflow.com/questions/12383246/why-does-setup-py-runs-the-package-init-py # NOQA
# so, this is a workaround to handle both
try:
    from flask import Flask
except ImportError:
    import sys
    sys.exit("You should not reach this point")

from flask.ext.mail import Mail


def config_app(app):
    # Load setting using various methods
    # TODO: do relative o package import
    app.config.from_object('VilfredoReloadedCore.defaults_settings')
    # TODO: document the VCR_VARIABLE
    app.config.from_envvar('VRC_SETTINGS', silent=True)

    from .database import init_engine
    init_engine(app.config['DATABASE_URI'])

app = Flask(__name__)
config_app(app)
mail = Mail(app)

# Logging
import logging
import logging.config

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Set logging
if (app.config['DEBUG']):
    # Set logging for development server here
    config_file = os.path.join(basedir, app.config['LOG_FILE'])
    logging.config.fileConfig(config_file)
    # create logger
    logger = logging.getLogger('vilfredo_logger')
    logger.propagate = False
else:
    # Set logging for production server here
    pass
