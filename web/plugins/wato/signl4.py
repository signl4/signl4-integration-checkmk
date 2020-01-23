#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# (c) 2020 Derdack GmbH
#          SIGNL4 <info@signl4.com>

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

register_notification_parameters("signl4", Dictionary(
    optional_keys = ['originator'],
    elements = [
        ("password", TextAscii(
            title = _("Team Secret"),
            help = _("The team secret of your SIGNL4 team. That is the last part of your webhook URL: https://connect.signl4.com/webhook/<team_secret>"),
            size = 40,
            allow_empty = False,
        )),
    ]
))
