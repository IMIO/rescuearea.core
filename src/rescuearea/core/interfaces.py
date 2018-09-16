# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.app.z3cform.interfaces import IPloneFormLayer


class IRescueareaCoreLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IRescueAreaFormLayer(IPloneFormLayer):
    """Request interface installed via browserlayer.xml"""
