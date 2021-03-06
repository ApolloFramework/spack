# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os.path
import inspect

from spack import *


class Grackle(Package):
    """Grackle is a chemistry and radiative cooling library for astrophysical
    simulations with interfaces for C, C++, and Fortran codes. It is a
    generalized and trimmed down version of the chemistry network of the Enzo
    simulation code
    """
    homepage = 'http://grackle.readthedocs.io/en/grackle-3.1/'
    url = 'https://bitbucket.org/grackle/grackle/get/grackle-3.1.tar.bz2'

    version('3.1', 'cee7799dc505010e2e875950561bbbe1')
    version('3.0', 'dc85e664da7e70b65b3ef7164477a959')
    version('2.2', 'ec49ed1db5a42db21f478285150c2ba3')
    version('2.0.1', 'a9624ad13a60c592c1a0a4ea8e1ae86d')

    variant('float', default=False, description='Build with float')

    depends_on('libtool', when='@2.2')

    depends_on('mpi')
    depends_on('hdf5+mpi')

    parallel = False

    def install(self, spec, prefix):
        template_name = '{0.architecture}-{0.compiler.name}'
        grackle_architecture = template_name.format(spec)
        link_variables = 'MACH_AR = ar' if spec.version < Version(2.2) else 'MACH_LIBTOOL = libtool'  # NOQA: ignore=E501
        substitutions = {
            '@ARCHITECTURE': grackle_architecture,
            '@CC': spec['mpi'].mpicc,
            '@CXX': spec['mpi'].mpicxx,
            '@FC': spec['mpi'].mpifc,
            '@F77': spec['mpi'].mpif77,
            '@STDCXX_LIB': ' '.join(self.compiler.stdcxx_libs),
            '@HDF5_ROOT': spec['hdf5'].prefix,
            '@PREFIX': prefix,
            '@LINK_VARIABLES_DEFINITION': link_variables
        }

        template = join_path(
            os.path.dirname(inspect.getmodule(self).__file__),
            'Make.mach.template'
        )
        makefile = join_path(
            self.stage.source_path,
            'src',
            'clib',
            'Make.mach.{0}'.format(grackle_architecture)
        )
        copy(template, makefile)
        for key, value in substitutions.items():
            filter_file(key, value, makefile)

        configure()
        with working_dir('src/clib'):
            make('clean')
            make('machine-{0}'.format(grackle_architecture))
            make('opt-high')
            if spec.satisfies("+float"):
                make('precision-32')
            make('show-config')
            make()
            mkdirp(prefix.lib)
            make('install')
