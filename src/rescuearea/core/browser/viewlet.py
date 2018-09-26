# -*- coding: utf-8 -*-

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import ViewletBase
from plone import api

from rescuearea.core import _

import datetime


class PopUpViewlet(ViewletBase):
    """ A viewlet which renders the popup """

    index = ViewPageTemplateFile('templates/popup.pt')

    def exist_popup(self):
        list_popup = api.content.find(context=self.context,
                                      portal_type='pop_up')

        if not list_popup:
            return False

        for popup in list_popup:
            today = datetime.date.today()
            start = popup.start
            end = popup.end
            if start <= today <= end:
                text = _(u'<p>From {0} to {1}').format(
                    start.strftime("%d-%m-%Y"),
                    end.strftime("%d-%m-%Y")
                )
                return '{0} {1}'.format(
                    text,
                    popup.getObject().richtext_desc.output
                )

        return False
