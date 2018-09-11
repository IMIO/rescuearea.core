# -*- coding: utf-8 -*-

from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implements
from zope.interface import Invalid
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

    start = schema.Date(
        title=_(u'Date start'),
        required=True,
    )

    end = schema.Date(
        title=_(u'Date end'),
        required=True,
    )

    @invariant
    def validate_start_end(data):
        if data.start is not None and data.end is not None:
            if data.start > data.end:
                raise Invalid(_(u"The start date must be before the end date."))


class PopUp(Container):
    implements(IPopUp)
