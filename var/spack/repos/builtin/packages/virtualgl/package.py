# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

#
from spack import *


class Virtualgl(CMakePackage):
    """VirtualGL redirects 3D commands from a Unix/Linux OpenGL application
       onto a server-side GPU and converts the rendered 3D images into a video
       stream with which remote clients can interact to view and control the
       3D application in real time."""

    homepage = "http://www.virtualgl.org/Main/HomePage"
    url      = "http://downloads.sourceforge.net/project/virtualgl/2.5.2/VirtualGL-2.5.2.tar.gz"

    version('2.5.2', '1a9f404f4a35afa9f56381cb33ed210c')

    depends_on("libjpeg-turbo")
    # virtualgl require OpenGL but also wants to link libglu
    # on systems without development packages, provide with spack and depends
    # on mesa-glu, but we do not want Mesa OpenGL sw emulation, so added
    # variant on mesa-glu to disable dependencies on sw emulated OpenGL
    depends_on("mesa-glu~mesa")
