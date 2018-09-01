# -*- coding: utf-8 -*-

from zope.interface import provider
from zope.i18n import translate
from zope.schema.interfaces import IContextAwareDefaultFactory
from zope.globalrequest import getRequest


def default_translator(msgstring, **replacements):
    @provider(IContextAwareDefaultFactory)
    def context_provider(context):
        value = translate(msgstring, context=getRequest())
        if replacements:
            value = value.format(**replacements)
        return value

    return context_provider
