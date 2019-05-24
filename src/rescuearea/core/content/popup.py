# -*- coding: utf-8 -*-

from datetime import datetime
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.indexer.decorator import indexer
from plone.supermodel import model
from zope import schema
from zope.interface import Invalid
from zope.interface import implements
from zope.interface import invariant

from rescuearea.core import _


class IPopUp(model.Schema):

    titre = schema.TextLine(
        title=_(u'Titre'),
        required=True,
    )

    richtext_desc = RichText(
        title=_(u'Description'),
        default_mime_type='text/html',
        required=True,
    )

    effective = schema.Date(
        title=_(u'Date start'),
        required=True,
    )

    expires = schema.Date(
        title=_(u'Date end'),
        required=True,
    )

    @invariant
    def validate_start_end(data):
        if data.effective is not None and data.expires is not None:
            if data.effective > data.expires:
                raise Invalid(_(u"The start date must be before the end date."))


class PopUp(Container):
    implements(IPopUp)

    @property
    def title(self):
        if hasattr(self, 'titre'):
            return self.titre

    @title.setter
    def title(self, value):
        self._title = value


@indexer(IPopUp)
def effective_indexer(object, **kwargs):
    return datetime.combine(object.effective, datetime.min.time())


@indexer(IPopUp)
def expires_indexer(object, **kwargs):
    return datetime.combine(object.expires, datetime.min.time())
