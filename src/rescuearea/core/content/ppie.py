# -*- coding: utf-8 -*-

from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from zope import schema
from zope.interface import implements

from rescuearea.core import _
from rescuearea.core.content.object_factory import ObjectField
from rescuearea.core.content.object_factory import register_object_factories
from rescuearea.core.utils import default_translator


class IMultidiciplinaryRowSchema(model.Schema):

    cce_event_coordination_cell = RichText(
        title=_(u'CCE Event Coordination Cell'),
        required=False,
        defaultFactory=default_translator(_(
            u'<p><span>Presence</span> :</p><p></p>'
            u'<p><span>Location</span> :</p>'
        )),
        default_mime_type='text/html',
    )

    centre_100 = RichText(
        title=_(u'Centre 100'),
        required=False,
    )


class IZHCMeansOnSiteRowSchema(model.Schema):

    schedule = schema.Datetime(
        title=_(u'Schedule'),
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


class IZHCExtraMeansAtTheFirstAidPostRowSchema(model.Schema):

    richtext_fields = RichText(
        required=False,
        defaultFactory=default_translator(_(
            u'<p><span>Human</span> :</p><p></p>'
            u'<p><span>Equipment</span> :</p>'
        )),
        default_mime_type='text/html',
    )

    schedule = schema.Datetime(
        title=_(u'Schedule'),
        required=False,
    )


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
        label=_(u'1 Description of the event'),
        fields=['dates_and_times',
                'location',
                'nature_and_risk_involved',
                'impacted_items',
                ]
    )

    dates_and_times = schema.Datetime(
        title=_(u'Dates and times'),
        required=False,
    )

    location = RichText(
        title=_(u'Location'),
        required=False,
    )

    nature_and_risk_involved = RichText(
        title=_(u'Nature and risk involved'),
        required=False,
        defaultFactory=default_translator(_(
            u'<p><span>Nature</span> :</p><p></p>'
            u'<p><span>Risks</span> :</p>'
        )),
        default_mime_type='text/html',
    )

    impacted_items = RichText(
        title=_(u'Impacted items'),
        required=False,
    )

    fieldset(
        'Impact on emergency stations',
        label=_(u'2 Impact on emergency stations'),
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
        label=_(u'3 Preventive devices'),
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
        label=_(u"4 Alert chain and communications"),
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
        required=False,
    )

    directory_and_telephone_directory = RichText(
        title=_(u'Directory and telephone directory'),
        required=False,
    )

    fieldset(
        'Rising power',
        label=_(u'5 Rising power'),
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
        required=False,
    )

    fieldset(
        'Miscellaneous remarks',
        label=_(u'6 Miscellaneous remarks'),
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
        label=_(u'7 Appendices'),
        fields=['appendices',
                ]
    )

    appendices = schema.List(
        title=_(u'Appendices'),
        required=False,
        value_type=RichText(title=_(u'Appendix')),
    )


class Ppie(Container):
    implements(IPpie)


register_object_factories(IPpie)
