# -*- coding: utf-8 -*-

from plone.formwidget.namedfile.interfaces import INamedFileWidget
from plone.formwidget.namedfile.widget import NamedFileWidget
from plone.namedfile.interfaces import INamedFileField
from z3c.form import interfaces
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.interface import Interface, implements, implementer


class IFileObjectWidget(Interface):
    """Marker interface for file object widget"""


class FileObjectWidget(NamedFileWidget):
    implements(IFileObjectWidget, INamedFileWidget)
    klass = u"named-file-widget"


@adapter(INamedFileField, interfaces.IFormLayer)
@implementer(interfaces.IFieldWidget)
def FileObjectFieldWidget(field, request):
    """IFieldWidget factory for FileObjectWidget"""
    return FieldWidget(field, FileObjectWidget(request))
