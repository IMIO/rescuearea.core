# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.textfield import RichText
from plone.dexterity.browser import add
from plone.dexterity.content import Container
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from zope import schema
from zope.interface import implements
from zope.interface import Invalid
from zope.interface import invariant

from rescuearea.core import _
from rescuearea.core.content.object_factory import ObjectField
from rescuearea.core.content.object_factory import register_object_factories
from rescuearea.core.utils import default_translator


class ICCEEventCoordinationCellRowSchema(model.Schema):

    present_location = RichText(
        title=_(u'Present and location'),
        required=False,
        defaultFactory=default_translator(_(
            u'<p><span>Presence</span> :</p><p></p>'
            u'<p><span>Location</span> :</p>'
        )),
        default_mime_type='text/html',
    )

    start = schema.Datetime(
        title=_(u'Schedule start'),
        required=False,
    )

    end = schema.Datetime(
        title=_(u'Schedule end'),
        required=False,
    )

    @invariant
    def validate_start_end(data):
        if data.start is not None and data.end is not None:
            if data.start > data.end:
                raise Invalid(_(u"The start date must be before the end date."))


class IMultidiciplinaryRowSchema(model.Schema):

    cce_event_coordination_cell = ObjectField(
        title=_(u'CCE Event Coordination Cell'),
        required=False,
        schema=ICCEEventCoordinationCellRowSchema
    )

    centre_100 = RichText(
        title=_(u'Centre 100'),
        required=False,
    )


class IZHCMeansOnSiteRowSchema(model.Schema):

    start = schema.Datetime(
        title=_(u'Schedule start'),
        required=False,
    )

    end = schema.Datetime(
        title=_(u'Schedule end'),
        required=False,
    )

    at_the_events_coordination_centre = RichText(
        title=_(u'At the events coordination centre (representative D1)'),
        required=False,
    )

    in_the_field = RichText(
        title=_(u'In the field (field PC)'),
        required=False,
    )

    @invariant
    def validate_start_end(data):
        if data.start is not None and data.end is not None:
            if data.start > data.end:
                raise Invalid(_(u"The start date must be before the end date."))


class IZHCExtraMeansAtTheFirstAidPostRowSchema(model.Schema):

    richtext_fields = RichText(
        required=False,
        defaultFactory=default_translator(_(
            u'<p><span>Human</span> :</p><p></p>'
            u'<p><span>Equipment</span> :</p>'
        )),
        default_mime_type='text/html',
    )

    start = schema.Datetime(
        title=_(u'Schedule start'),
        required=False,
    )

    end = schema.Datetime(
        title=_(u'Schedule end'),
        required=False,
    )

    @invariant
    def validate_start_end(data):
        if data.start is not None and data.end is not None:
            if data.start > data.end:
                raise Invalid(_(u"The start date must be before the end date."))


class IDiscipline1RowSchema(model.Schema):

    zhc_means_on_site = ObjectField(
        title=_(u'Z.H.C. means on site'),
        schema=IZHCMeansOnSiteRowSchema,
        required=False,
    )

    organizing_means_on_site = RichText(
        title=_(u'Organizing means on site (for info)'),
        required=False,
    )

    zhc_extra_means_at_the_first_aid_post = ObjectField(
        title=_(u'Z.H.C. extra means at the first aid post'),
        schema=IZHCExtraMeansAtTheFirstAidPostRowSchema,
        required=False,
    )


class IDiscipline2RowSchema(model.Schema):

    Location_ps_pma = RichText(
        title=_(u'Location P.S.,P.M.A.'),
        required=False,
    )

    organizing_means_on_site = RichText(
        title=_(u'Organizing means on site (for info)'),
        required=False,
    )

    zhc_extra_means_at_the_first_aid_post = RichText(
        title=_(u'Z.H.C. extra means at the first aid post'),
        required=False,
    )


class IPpie(model.Schema):
    """IPpie"""

    fieldset(
        'Description of the event',
        label=_(u'Description of the event'),
        fields=['start',
                'end',
                'location',
                'nature_and_risk_involved',
                'impacted_items',
                ]
    )

    start = schema.Datetime(
        title=_(u'Dates and times start'),
        required=True,
    )

    end = schema.Datetime(
        title=_(u'Dates and times stop'),
        required=True,
    )

    location = RichText(
        title=_(u'Location'),
        required=True,
    )

    nature_and_risk_involved = RichText(
        title=_(u'Nature and risk involved'),
        required=True,
        defaultFactory=default_translator(_(
            u'<p><span>Nature</span> :</p><p></p>'
            u'<p><span>Risks</span> :</p>'
        )),
        default_mime_type='text/html',
    )

    impacted_items = RichText(
        title=_(u'Impacted items'),
        required=True,
    )

    fieldset(
        'Impact on emergency stations',
        label=_(u'Impact on emergency stations'),
        fields=['modified_itinerary',
                'access_to_the_site_for_firefighters',
                'access_for_ambulances',
                ]
    )

    modified_itinerary = RichText(
        title=_(u'Modified itinerary'),
        required=False,
    )

    access_to_the_site_for_firefighters = RichText(
        title=_(u'Access to the site for firefighters'),
        required=False,
    )

    access_for_ambulances = RichText(
        title=_(u'Access for ambulances'),
        required=False,
    )

    fieldset(
        'Preventive devices',
        label=_(u'Preventive devices'),
        fields=['multidiciplinary',
                'discipline1',
                'discipline2',
                ]
    )

    multidiciplinary = ObjectField(
        title=_(u'Multidiciplinary'),
        schema=IMultidiciplinaryRowSchema,
        required=False,
    )

    discipline1 = ObjectField(
        title=_(u'Discipline 1'),
        schema=IDiscipline1RowSchema,
        required=False,
    )

    discipline2 = ObjectField(
        title=_(u'Discipline é'),
        schema=IDiscipline2RowSchema,
        required=False,
    )

    fieldset(
        'Alert chain and communications',
        label=_(u"Alert chain and communications"),
        fields=['on_site_intervention_request_management',
                'communication_radio',
                'directory_and_telephone_directory',
                ]
    )

    on_site_intervention_request_management = RichText(
        title=_(u'On-site intervention request management'),
        required=False,
    )

    communication_radio = RichText(
        title=_(u'Communication radio'),
        required=True,
    )

    directory_and_telephone_directory = RichText(
        title=_(u'Directory and telephone directory'),
        required=False,
    )

    fieldset(
        'Rising power',
        label=_(u'Rising power'),
        fields=['access_to_the_site',
                'means',
                'location_ppd',
                'location_pc_ops',
                'location_municipal_crisis_centre',
                ]
    )

    access_to_the_site = RichText(
        title=_(u'Access to the site'),
        required=False,
    )

    means = RichText(
        title=_(u'Means'),
        required=False,
    )

    location_ppd = RichText(
        title=_(u'Location P.P.D.'),
        required=False,
    )

    location_pc_ops = RichText(
        title=_(u'Location P.C. OPS'),
        required=False,
    )

    location_municipal_crisis_centre = RichText(
        title=_(u'Location municipal crisis centre'),
        required=True,
    )

    fieldset(
        'Miscellaneous remarks',
        label=_(u'Miscellaneous remarks'),
        fields=['preliminary_actions_to_be_undertaken',
                'contact_person_for_information_on_this_document',
                ]
    )

    preliminary_actions_to_be_undertaken = RichText(
        title=_(u'Preliminary actions to be undertaken'),
        required=False,
    )

    contact_person_for_information_on_this_document = RichText(
        title=_(u'Contact person for information on this document'),
        required=False,
    )

    fieldset(
        'Appendices',
        label=_(u'Appendices'),
        fields=['appendices',
                ]
    )

    appendices = schema.List(
        title=_(u'Appendices'),
        required=False,
        value_type=RichText(title=_(u'Appendix')),
    )

    @invariant
    def validate_start_end(data):
        if data.start is not None and data.end is not None:
            if data.start > data.end:
                raise Invalid(_(u"The start date must be before the end date."))


class Ppie(Container):
    implements(IPpie)


class AddForm(add.DefaultAddForm, BrowserView):
    portal_type = 'ppi_e'
    template = ViewPageTemplateFile('templates/ppie_form_add.pt')

    def update(self):
        super(add.DefaultAddForm, self).update()
        for group in self.groups:
            if group.__name__ == "dates":
                group.fields["IDublinCore.effective"].field.required = True
                group.fields["IDublinCore.expires"].field.required = True


class AddView(add.DefaultAddView):
    form = AddForm


register_object_factories(IPpie)
