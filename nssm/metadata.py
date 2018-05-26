# -*- coding: utf-8 -*-
"""
 Project metadata
 Information describing the project.

 Created on May 19, 2018
 @author: Lorenzo Delgado <lorenzo.delgado@lnsd.es>
"""

# The package name, which is also the "UNIX name" for the project.
package = 'pynssm'
project = "PyNSSM"
project_no_spaces = project.replace(' ', '')
version = '2.24.1-alpha.3'
description = 'Python wrapper for NSSM - the Non-Sucking Service Manager (nssm.cc)'
authors = ['Lorenzo Delgado']
authors_string = ', '.join(authors)
emails = ['lorenzo.delgado@lnsd.es']
license = 'MIT'
copyright = '2018 ' + authors_string
url = 'https://github.com/LNSD/pynssm'
download_url = 'https://github.com/LNSD/pynssm/archive/{}.tar.gz'.format(version)
