# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Patch(Package):
    """Package that requries a patched version of a dependency."""

    homepage = "http://www.example.com"
    url = "http://www.example.com/patch-1.0.tar.gz"

    version('1.0', '0123456789abcdef0123456789abcdef')

    patch('foo.patch')
    patch('bar.patch')
    patch('baz.patch')

    def install(self, spec, prefix):
        pass
