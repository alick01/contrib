#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import scons
from pisi.actionsapi import get


def setup():
	autotools.configure("--prefix=/usr")


def build():
    autotools.make()

def install():	
	shelltools.system("cd src")
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.insinto("/usr/share/pixmaps/", "data/atari2.png", "atari800.png")
	pisitools.dodir("/usr/share/atari800")
	pisitools.dodir("/etc")
	pisitools.dodoc("COPYING", "README.TXT*")
