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
        list_popup = api.content.find(
            context=self.context,
            portal_type='pop_up',
        )

        if not list_popup:
            return False

        for popup in list_popup:
            if popup.EffectiveDate != 'None':
                today = datetime.date.today()
                start = popup.effective.date()
                end = popup.expires.date()
                if start <= today <= end:
                    text = _(u"popup_message",
                             default=u'<p>From ${start} to ${end}</p> <p>${message}</p>',
                             mapping={u"start": start.strftime("%d-%m-%Y"),
                                      u"end": end.strftime("%d-%m-%Y"),
                                      u"message": popup.getObject().richtext_desc.output}
                             )
                    return text

        return False
