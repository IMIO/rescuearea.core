# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from rescuearea.core import _
from plone.autoform import directives as form
from zope import schema
from zope.interface import Interface


class IAnomaliesReportingSettingsSchema(Interface):

    form.widget("anomalies_reporting", klass="pat-tinymce")
    anomalies_reporting = schema.Text(title=_(u"Anomalies reporting settings"))


class AnomaliesReportingSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IAnomaliesReportingSettingsSchema
    label = _(u"Anomalies reporting settings")
    description = _(u"")

    def updateFields(self):
        super(AnomaliesReportingSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(AnomaliesReportingSettingsEditForm, self).updateWidgets()


class AnomaliesReportingSettingsControlPanel(
    controlpanel.ControlPanelFormWrapper
):  # noqa: E501
    form = AnomaliesReportingSettingsEditForm
