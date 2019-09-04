# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from plone import api


class AnomaliesReportingView(BrowserView):
    """AnomaliesReportingView"""

    def get_settings_value(self):
        return api.portal.get_registry_record(
            "rescuearea.core.browser.controlpanel.IAnomaliesReportingSettingsSchema.anomalies_reporting"
        )  # noqa: E501
