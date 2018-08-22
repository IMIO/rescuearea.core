# -*- coding: utf-8 -*-

from rescuearea.core import _

from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implements
from zope import schema
from plone.app.textfield import RichText
from plone.supermodel.directives import fieldset
from plone.namedfile.field import NamedBlobFile


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


class IAddressRowSchema(model.Schema):

    number = schema.TextLine(
        title=_(u"N°"),
        required=False,
    )

    street = schema.TextLine(
        title=_(u"Street"),
        required=True,
    )

    zip_code = schema.Int(
        title=_(u"Zip code"),
        required=True,
    )

    commune = schema.TextLine(
        title=_(u"Commune"),
        required=True,
    )

    longitude = schema.Float(
        title=_(u"Longitude"),
        required=False,
    )

    latitude = schema.Float(
        title=_(u"Latitude"),
        required=False,
    )


class IOccupancyScheduleRowSchema(model.Schema):

    schedule = schema.TextLine(
        title=_(u"Schedule"),
        required=False,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )


class IKeysCodeAccessBadgeFieldsRowSchema(model.Schema):

    description_and_usefulness_of_keys = RichText(
        title=_(u"Description and Usefulness of Keys"),
        required=False,
    )

    key_storage_location = RichText(
        title=_(u"Key Storage Location"),
        required=False,
    )

    number_of_copies = schema.Int(
        title=_(u"Number of Copies"),
        required=False,
    )

    last_key_check_date = schema.Datetime(
        title=_(u"Last Key Check Date"),
        required=False,
    )


class ILinkFileRowSchema(model.Schema):

    file = NamedBlobFile(
        title=_(u"File"),
        required=False,
    )

    link = schema.URI(
        title=_(u"Link"),
        required=False,
    )


class IHistoryRowSchema(model.Schema):

    modified_field = schema.TextLine(
        title=_(u"Modified field"),
        required=False,
    )

    date = schema.Date(
        title=_(u"Date"),
        required=False,
    )

    user = schema.TextLine(
        title=_(u"User"),
        required=False,
    )


class IPpi(model.Schema):
    """IPpi"""

    fieldset(
        'description sheet',
        label=_(u"1 Description sheet"),
        fields=['site_name',
                'other_names',
                'address',
                'occupancy_schedule',
                'type_of_activity',
                'concierge_service',
                'contacts',
                'premises',
                'existence_of_a_ppui',
                'data_limited_to_description',
                'site_classified_seveso',
                'keys_code_access_badge',
                'keys_code_access_badge_fields',
                'date_of_update_of_the_description_sheet',
                ]
    )

    site_name = schema.TextLine(
        title=_(u"Site name"),
        required=True,
    )

    other_names = schema.TextLine(
        title=_(u"Other names"),
        required=False,
    )

    address = schema.Object(
        title=_(u"Address"),
        schema=IAddressRowSchema,
        required=True,
    )

    occupancy_schedule = schema.Object(
        title=_(u"Occupancy schedule"),
        schema=IOccupancyScheduleRowSchema,
        required=False,
    )

    type_of_activity = schema.TextLine(
        title=_(u"Type of activity"),
        required=False,
    )

    concierge_service = schema.Bool(
        title=_(u"Concierge Service?"),
        required=False,
    )

    contacts = schema.List(
        title=_(u"Contacts"),
        required=False,
        value_type=schema.Object(
            title=_(u"Contacts"),
            schema=IContactRowSchema
        ),
    )

    premises = RichText(
        title=_(u"Premises"),
        required=False,
    )

    existence_of_a_ppui = schema.Text(
        title=_(u"Existence of a PPUI?"),
        required=False,
    )

    data_limited_to_description = schema.Bool(
        title=_(u"Data limited to description?"),
        required=False,
    )

    site_classified_seveso = schema.Choice(
        title=_(u"Site classified SEVESO?"),
        vocabulary=u'rescuearea.core.vocabularies.seveso',
        required=False,
    )

    keys_code_access_badge = schema.Bool(
        title=_(u"Keys, code, access badge? "),
        required=False,
    )

    keys_code_access_badge_fields = schema.Object(
        schema=IKeysCodeAccessBadgeFieldsRowSchema,
        required=False,
    )

    date_of_update_of_the_description_sheet = schema.Datetime(
        title=_(u"Date of update of the description sheet"),
        required=False,
    )

    fieldset(
        'before departure',
        label=_(u"2 Before departure"),
        fields=['adaptation_of_the_emergency_services_in_relation_to_the_response_plan',
                'specific_equipment_to_take_with_you',
                'route_to_follow',
                'site_particularities',
                'instructions_for_the_operator',
                ]
    )

    adaptation_of_the_emergency_services_in_relation_to_the_response_plan = RichText(
        title=_(u"Adaptation of the emergency services in relation to the response plan"),
        required=False,
    )

    specific_equipment_to_take_with_you = RichText(
        title=_(u"Specific equipment to take with you"),
        required=False,
    )

    route_to_follow = RichText(
        title=_(u"Route to follow"),
        required=False,
    )

    site_particularities = RichText(
        title=_(u"Site Particularities"),
        required=False,
    )

    instructions_for_the_operator = RichText(
        title=_(u"Instructions for the operator"),
        required=False,
    )

    fieldset(
        'during the ride',
        label=_(u"3 During the ride"),
        fields=['vehicle_stop_emergency_reception_point',
                'point_of_first_destination',
                ]
    )

    vehicle_stop_emergency_reception_point = RichText(
        title=_(u"Vehicle stop/emergency reception point"),
        required=False,
    )

    point_of_first_destination = RichText(
        title=_(u"Point of First Destination (PFD)"),
        required=False,
    )

    fieldset(
        'on_site',
        label=_(u"4 On site "),
        fields=['reflex_measurements_on_arrival_on_site',
                'special_means_of_protection_to_wear',
                'risks_present',
                'materials_equipment_available',
                ]
    )

    reflex_measurements_on_arrival_on_site = RichText(
        title=_(u"Reflex measurements on arrival on site"),
        required=False,
    )

    special_means_of_protection_to_wear = RichText(
        title=_(u"Special means of protection to wear"),
        required=False,
    )

    risks_present = RichText(
        title=_(u"Risks Present"),
        required=False,
    )

    materials_equipment_available = RichText(
        title=_(u"Materials/Equipment available"),
        required=False,
    )

    fieldset(
        'additional_information',
        label=_(u"5 Additional information"),
        fields=['appendix_itinerary',
                'appendix_map_of_the_location',
                'appendix_implementation_plan',
                'appendix_water_resources',
                'appendix_axonometric_view',
                'appendix_carroyer_plan',
                'appendix_description',
                ]
    )

    appendix_itinerary = NamedBlobFile(
        title=_(u'Appendix : Itinerary'),
        required=False,
    )

    appendix_map_of_the_location = schema.Object(
        title=_(u"Appendix : Map of the location"),
        schema=ILinkFileRowSchema,
        required=False,
    )

    appendix_implementation_plan = NamedBlobFile(
        title=_(u'Appendix : Implementation Plan'),
        required=False,
    )

    appendix_water_resources = schema.Object(
        title=_(u"Appendix : Water resources "),
        schema=ILinkFileRowSchema,
        required=False,
    )

    appendix_axonometric_view = NamedBlobFile(
        title=_(u'Appendix : Axonometric view'),
        required=False,
    )

    appendix_carroyer_plan = NamedBlobFile(
        title=_(u'Appendix : Carroyer plan'),
        required=False,
    )

    appendix_description = NamedBlobFile(
        title=_(u'Appendix : Description'),
        required=False,
    )

    fieldset(
        'Return to normal',
        label=_(u"6 Return to normal"),
        fields=['attention_points_for_the_return_to_normal',
                ]
    )

    attention_points_for_the_return_to_normal = RichText(
        title=_(u"Attention points for the return to normal"),
        required=False,
    )

    fieldset(
        'Administration of PPI',
        label=_(u"7 Administration of PPI"),
        fields=['ppi_reference',
                'date_of_last_modification',
                'deadline_for_searching_for_additional_information',
                'modification_history',
                'case_officer',
                'preventionist',
                'availability_of_paper_copies',
                'classification_for_risk_analysis',
                ]
    )

    ppi_reference = schema.TextLine(
        title=_(u"PPI reference"),
        required=True,
    )

    date_of_last_modification = schema.Datetime(
        title=_(u"Date of last modification"),
        required=False,
    )

    deadline_for_searching_for_additional_information = schema.Date(
        title=_(u"Deadline for searching for additional information"),
        required=False,
    )

    modification_history = schema.List(
        title=_(u"Modification history"),
        required=False,
        value_type=schema.Object(
            title=_(u"History"),
            schema=IHistoryRowSchema
        ),
    )

    case_officer = schema.TextLine(
        title=_(u"case_officer"),
        required=False,
    )

    preventionist = schema.TextLine(
        title=_(u"Preventionist"),
        required=False,
    )

    availability_of_paper_copies = schema.Text(
        title=_(u"Availability of Paper Copies"),
        required=False,
    )

    classification_for_risk_analysis = schema.Choice(
        title=_(u"Classification for risk analysis"),
        vocabulary=u'rescuearea.core.vocabularies.classification',
        required=False,
    )


class Ppi(Container):
    implements(IPpi)
