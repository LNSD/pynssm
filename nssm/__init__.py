# -*- coding: utf-8 -*-
"""
 Python wrapper for NSSM

 Created on May 19, 2018
 @author: Lorenzo Delgado <lorenzo.delgado@lnsd.es>
"""
from nssm import metadata

__version__ = metadata.version
__author__ = metadata.authors[0]
__license__ = metadata.license
__copyright__ = metadata.copyright


from .service import Service, ServiceStatus  # NOQA
from .configuration import ServiceConfiguration  # NOQA
from .parameters import StartupType, PriorityLevel, ServiceType, ExitAction  # NOQA
from .exceptions import *  # NOQA

# NSSM executable path
from .wrapper import executable   # NOQA
