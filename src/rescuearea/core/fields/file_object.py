# -*- coding: utf-8 -*-

import zope.interface
import zope.schema
from plone.namedfile.field import NamedBlobFile
from plone.namedfile.interfaces import INamedBlobFileField


class IFileObject(INamedBlobFileField):
    """ """


class FileObject(NamedBlobFile):
    zope.interface.implements(IFileObject)
