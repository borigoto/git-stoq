# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Copyright (C) 2005 Async Open Source
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU Lesser General Public License
## as published by the Free Software Foundation; either version 2
## of the License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., or visit: http://www.gnu.org/.
##
##
## Author(s):       Evandro Vale Miquelito      <evandro@async.com.br>
##                  Henrique Romano             <henrique@async.com.br>
##
""" Exception and warning definitions """


class ConfigError(Exception):
    """Error for config files which don't have a certain section"""


class FilePermissionError(Exception):
    """General error for file permissions."""


class NoConfigurationError(Exception):
    """Raise this error when we don't have a config option properly set."""


class ModelDataError(Exception):
    """General model data errors """


class SellError(Exception):
    """Exceptions for sale operations"""


class DatabaseInconsistency(Exception):
    """Exceptions for missing data or inconsistency"""


class DatabaseError(Exception):
    """General database errors"""


class StockError(Exception):
    """Exception for stock operations"""


class EditorError(Exception):
    """Exception for stoqlib editors"""


class SelectionError(Exception):
    """Invalid number of items selected in a list"""


class TillError(Exception):
    """ General Till operation errors """


class PaymentError(Exception):
    """ General payment errors """


class PaymentMethodError(Exception):
    """Error for payment methods"""


class AdapterError(Exception):
    """Raise this exception when an object try adding a facet but it doesn't
    actually implements that interface"""


class UserProfileError(Exception):
    """Raise when a certain user lacks credentials for an application"""


class LoginError(Exception):
    """Raise when an username or password is invalid"""

class SQLError(Exception):
    """Bad syntax for sql scripts"""
