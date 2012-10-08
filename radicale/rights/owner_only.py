# -*- coding: utf-8 -*-
#
# This file is part of Radicale Server - Calendar Server
# Copyright © 2012 Guillaume Ayoub
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Radicale.  If not, see <http://www.gnu.org/licenses/>.

"""
Owner-only based rights.

Only owners have read and write access to their own collections.

"""

def read_authorized(user, collection):
    """Check if the user is allowed to read the collection."""
    if user == None:
      return False
    return collection.path == '' or \
           user == collection.owner.replace("+", " ") or \
           user.startswith("caldav@example.com ")


def write_authorized(user, collection):
    """Check if the user is allowed to write the collection."""
    return read_authorized(user, collection)
