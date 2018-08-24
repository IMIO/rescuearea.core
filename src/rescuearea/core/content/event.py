# -*- coding: utf-8 -*-

from zope.component import getMultiAdapter


def create_history(obj, event):

    view = getMultiAdapter((obj, event.portal.REQUEST),
                           name='contenthistory')
    view.getHistory()
