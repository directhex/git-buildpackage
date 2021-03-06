#!/usr/bin/python
# Copyright (C) 2006,2007 Guido Guenther <agx@sigxcpu.org>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# END OF COPYRIGHT #

from distutils.core import setup

setup(name = "git_build_package",
      author = 'Guido Guenther',
      author_email = 'agx@sigxcpu.org',
      scripts = [ 'git-buildpackage', 'git-import-dsc', 'git-import-orig', 'git-dch', 'git-import-dscs',
                  'gbp-pq', 'gbp-pull', 'gbp-clone', 'git-pbuilder' ],
      packages = [ 'gbp' ],
      data_files = [("/etc/git-buildpackage/", ["gbp.conf" ]),],
)

