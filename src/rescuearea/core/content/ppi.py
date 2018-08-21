# -*- coding: utf-8 -*-

from rescuearea.core import _

from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implements
from zope import schema
from plone.app.textfield import RichText


class IContactRowSchema(model.Schema):

    priority = schema.TextLine(
        title=_(u"Priority"),
        required=False,
    )

    function = schema.TextLine(
        title=_(u"Function"),
        required=False,
    )

    phone = schema.TextLine(
        title=_(u"Phone"),
        required=False,
    )

    remark = schema.TextLine(
        title=_(u"Remark"),
        required=False,
    )


class IPpi(model.Schema):
    """IPpi"""

    model.Fieldset(
        'description sheet',
        label=_(u"1 Description sheet"),
        fields=['site_name',
                'other_names',
                'address',
                'occupancy schedule',
                'type_of_activity',
                'contacts',
                'premises',
                'existence_of_a_ppui',
                'data_limited_to_description',
                'site_classified_seveso',
                'keys_code_access_badge',
                'keys_code_access_badge_fields',
                'Date_of_update_of_the_description_sheet']
    )

    site_name = schema.TextLine(
        title=_(u"1.1 Site name"),
        required=False,
    )

    other_names = schema.TextLine(
        title=_(u"1.2 Other names"),
        required=False,
    )

    model.Fieldset(
        'address',
        label=_(u"1.3 Address"),
        fields=['number',
                'street',
                'zip_code',
                'commune',
                'longitude',
                'latitude']
    )

    number = schema.TextLine(
        title=_(u"N°"),
        required=False,
    )

    street = schema.TextLine(
        title=_(u"Street"),
        required=False,
    )

    zip_code = schema.Int(
        title=_(u"Zip code"),
        required=False,
    )

    commune = schema.TextLine(
        title=_(u"Commune"),
        required=False,
    )

    longitude = schema.Float(
        title=_(u"Longitude"),
        required=False,
    )

    latitude = schema.Float(
        title=_(u"Latitude"),
        required=False,
    )

    model.Fieldset(
        'occupancy schedule',
        label=_(u"1.4 Occupancy schedule"),
        fields=['schedule',
                'description']
    )

    schedule = schema.TextLine(
        title=_(u"Schedule"),
        required=False,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    type_of_activity = schema.TextLine(
        title=_(u"1.5 Type of activity"),
        required=False,
    )

    concierge_service = schema.Bool(
        title=_(u"1.6 Concierge Service?"),
        required=False,
    )

    contacts = schema.List(
        title=_(u"1.7 Contacts"),
        required=False,
        value_type=schema.Object(
            title=_(u"Contacts"),
            schema=IContactRowSchema
        )
    )

    premises = RichText(
        title=_(u"1.8 Premises"),
        required=False
    )

    existence_of_a_ppui = schema.Text(
        title=_(u"1.9 Existence of a PPUI?"),
        required=False
    )

    data_limited_to_description = schema.Bool(
        title=_(u"1.10 Data limited to description?"),
        required=False,
    )

    site_classified_seveso = schema.Choice(
        title=_(u"1.11 Site classified SEVESO?"),
        vocabulary=u'rescuearea.core.vocabularies.seveso',
        required=False
    )

    keys_code_access_badge = schema.Bool(
        title=_(u"1.12 Keys, code, access badge? "),
        required=False,
    )

    model.Fieldset(
        'keys_code_access_badge_fields',
        label=_(u"keys_code_access_badge_fields"),
        fields=['description_and_usefulness_of_keys',
                'key_storage_location',
                'number_of_copies',
                'last_key_check_date']
    )

    description_and_usefulness_of_keys = RichText(
        title=_(u"1.12.1 Description and Usefulness of Keys"),
        required=False
    )

    key_storage_location = RichText(
        title=_(u"1.12.2 Key Storage Location"),
        required=False
    )

    number_of_copies = schema.Int(
        title=_(u"1.12.3 Number of Copies"),
        required=False,
    )

    last_key_check_date = schema.Datetime(
        title=_(u"1.12.4 Last Key Check Date"),
        required=False,
    )

    Date_of_update_of_the_description_sheet = schema.Datetime(
        title=_(u"1.13 Date of update of the description sheet"),
        required=False,
    )

    model.Fieldset(
        'before departure',
        label=_(u"2 Before departure"),
        fields=['site_name']
    )


class Ppi(Container):
    implements(IPpi)
