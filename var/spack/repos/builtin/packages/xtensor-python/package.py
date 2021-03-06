# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class XtensorPython(CMakePackage):
    """Python bindings for the xtensor C++ multi-dimensional array library"""

    homepage = "https://xtensor-python.readthedocs.io"
    url      = "https://github.com/QuantStack/xtensor-python/archive/0.17.0.tar.gz"
    git      = "https://github.com/QuantStack/xtensor-python.git"

    maintainers = ['ax3l']

    version('develop', branch='master')
    version('0.17.0', '51d22e42909a81201c3421d9e119eed0')

    depends_on('xtensor@0.15.1:0.15.99', when='@0.17.0:')
    depends_on('xtl@0.4.0:0.4.99', when='@0.17.0:')
    depends_on('py-pybind11@2.2.1', when='@0.17.0:')

    depends_on('py-numpy')
    depends_on('python', type=('build', 'link', 'run'))

    extends('python')

    def cmake_args(self):
        spec = self.spec

        python_exe = spec['python'].command.path

        args = [
            '-DPYTHON_EXECUTABLE={0}'.format(python_exe)
        ]
        return args
