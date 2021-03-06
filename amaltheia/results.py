# Copyright (C) 2019  GRNET S.A.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from amaltheia.utils import colored

colors = {
    'evacuated': 'yellow',
    'failed': 'red',
    'updated': 'green',
    'restored': 'magenta'
}


class HostResult(object):
    def __init__(self, **kwargs):

        self.evacuated = False
        self.updated = 0
        self.failed = 0
        self.restored = False
        self.exception = False

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        items = []
        for key, value in self.__dict__.items():
            if key == 'host_name' or key == 'exception' and not value:
                continue

            if str(value) == '0':
                color = None
            elif str(value) == 'False' and key != 'exception':
                color = 'red'
            else:
                color = colors.get(key)

            items.append(colored('{}={}'.format(key, value), color))

        return '{}{}'.format(self.host_name.ljust(50), ' '.join(items))
