# -*- coding: utf-8 -*-


from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from zope import schema
from zope.interface import implements

from rescuearea.core import _
from rescuearea.core.content.object_factory import ObjectField
from rescuearea.core.content.object_factory import register_object_factories
from rescuearea.core.utils import default_translator


occupation_table_value = (
    u'<table border="1"><tbody><tr>'
    u'<td><h6>00h00</h6></td>'
    u'<td><h6>01h00</h6></td>'
    u'<td><h6>02h00</h6></td>'
    u'<td><h6>03h00</h6></td>'
    u'<td><h6>04h00</h6></td>'
    u'<td><h6>05h00</h6></td>'
    u'<td><h6>06h00</h6></td>'
    u'<td><h6>07h00</h6></td>'
    u'<td><h6>08h00</h6></td>'
    u'<td><h6>09h00</h6></td>'
    u'<td><h6>10h00</h6></td>'
    u'<td><h6>11h00</h6></td>'
    u'<td><h6>12h00</h6></td>'
    u'<td><h6>13h00</h6></td>'
    u'<td><h6>14h00</h6></td>'
    u'<td><h6>15h00</h6></td>'
    u'<td><h6>16h00</h6></td>'
    u'<td><h6>17h00</h6></td>'
    u'<td><h6>18h00</h6></td>'
    u'<td><h6>19h00</h6></td>'
    u'<td><h6>20h00</h6></td>'
    u'<td><h6>21h00</h6></td>'
    u'<td><h6>22h00</h6></td>'
    u'<td><h6>23h00</h6></td>'
    u'</tr><tr>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'<td>0</td>'
    u'</tr></tbody></table>'
    u'<div class="page" title="Page 1"><p></p></div>'
)


class IContactRowSchema(model.Schema):
    priority = schema.TextLine(
        title=_(u'Priority'),
        required=False,
    )

    function = schema.TextLine(
        title=_(u'Function'),
        required=False,
    )

    phone = schema.TextLine(
        title=_(u'Phone'),
        required=False,
    )

    remark = schema.TextLine(
        title=_(u'Remark'),
        required=False,
    )


class IAddressRowSchema(model.Schema):
    number = schema.TextLine(
        title=_(u'N°'),
        required=False,
    )

    street = schema.TextLine(
        title=_(u'Street'),
        required=True,
    )

    zip_code = schema.Int(
        title=_(u'Zip code'),
        required=True,
    )

    commune = schema.TextLine(
        title=_(u'Commune'),
        required=True,
    )

    longitude = schema.Float(
        title=_(u'Longitude'),
        required=False,
    )

    latitude = schema.Float(
        title=_(u'Latitude'),
        required=False,
    )


class IOccupancyScheduleRowSchema(model.Schema):
    schedule = schema.TextLine(
        title=_(u'Schedule'),
        required=False,
    )

    description = RichText(
        title=_(u'Description'),
        default_mime_type='text/html',
        defaultFactory=default_translator(
            _(
                u'{table}<div><div class="column">'
                u'<p><span>0 No activity</span></p>'
                u'<p><span>1 Workers present</span></p>'
                u'<p><span>2 Open to public</span></p>'
                u'</div></div>'
            ),
            table=occupation_table_value,
        ),
        required=False,
    )


class IKeysCodeAccessBadgeFieldsRowSchema(model.Schema):

    keys_code_access_badge = RichText(
        title=_(u'Information'),
        required=False,
        default_mime_type='text/html',
        defaultFactory=default_translator(_(
            u'<p>Description and usefulness of the keys :</p>'
            u'<p>Where the key is stored :</p>'
            u'<p>Number of copies :</p>'
        )),
    )

    last_key_check_date = schema.Datetime(
        title=_(u'Last Key Check Date'),
        required=False,
    )


class ILinkFileRowSchema(model.Schema):
    file = NamedBlobFile(
        title=_(u'File'),
        required=False,
    )

    link = schema.URI(
        title=_(u'Link'),
        required=False,
    )


class IHistoryRowSchema(model.Schema):
    modified_field = schema.TextLine(
        title=_(u'Modified field'),
        required=False,
    )

    date = schema.Date(
        title=_(u'Date'),
        required=False,
    )

    user = schema.TextLine(
        title=_(u'User'),
        required=False,
    )


class IPpi(model.Schema):
    """IPpi"""

    fieldset(
        'description sheet',
        label=_(u'1 Description sheet'),
        fields=['title',
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

    title = schema.TextLine(
        title=_(u'Site name'),
        required=True,
    )

    other_names = schema.TextLine(
        title=_(u'Other names'),
        required=False,
    )

    address = ObjectField(
        title=_(u'Address'),
        schema=IAddressRowSchema,
        required=True,
    )

    occupancy_schedule = ObjectField(
        title=_(u'Occupancy schedule'),
        description=_(u'<p>Specify night occupancy or not. Specify public occupation</p>'),
        schema=IOccupancyScheduleRowSchema,
        required=False,
    )

    type_of_activity = schema.TextLine(
        title=_(u'Type of activity'),
        description=_(u'<p>Factory, warehouse, store, MRPA... Public access, number of people, valid? autonomous? sleeping? Describe in a few lines what it is about.</p>'),
        required=False,
    )

    concierge_service = schema.Bool(
        title=_(u'Concierge Service?'),
        required=False,
    )

    contacts = schema.List(
        title=_(u'Contacts'),
        required=False,
        value_type=ObjectField(
            title=_(u'Contacts'),
            schema=IContactRowSchema
        ),
    )

    premises = RichText(
        title=_(u'Premises'),
        required=False,
    )

    existence_of_a_ppui = schema.Text(
        title=_(u'Existence of a PPUI?'),
        description=_(u'<p>If yes, briefly describe the multidisciplinary principles...</p>'),
        required=False,
    )

    data_limited_to_description = schema.Bool(
        title=_(u'Data limited to description?'),
        required=False,
    )

    site_classified_seveso = schema.Choice(
        title=_(u'Site classified SEVESO?'),
        vocabulary=u'rescuearea.core.vocabularies.seveso',
        required=False,
    )

    keys_code_access_badge = schema.Bool(
        title=_(u'Keys, code, access badge?'),
        description=_(u'If yes, describe utility'),
        required=False,
    )

    keys_code_access_badge_fields = ObjectField(
        schema=IKeysCodeAccessBadgeFieldsRowSchema,
        required=False,
    )

    date_of_update_of_the_description_sheet = schema.Datetime(
        title=_(u'Date of update of the description sheet'),
        required=False,
    )

    fieldset(
        'before departure',
        label=_(u'2 Before departure'),
        fields=['adaptation_of_the_emergency_services_in_relation_to_the_response_plan',
                'specific_equipment_to_take_with_you',
                'route_to_follow',
                'site_particularities',
                'instructions_for_the_operator',
                ]
    )

    adaptation_of_the_emergency_services_in_relation_to_the_response_plan = RichText(
        title=_(u'Adaptation of the emergency services in relation to the response plan'),
        description=_(u'<p>How should the dispatch of help be adapted for this site in relation to the usual procedures?</p>'),
        required=False,
    )

    specific_equipment_to_take_with_you = RichText(
        title=_(u'Specific equipment to take with you'),
        description=_(u'<p>For example UHF relay for buildings with insufficient UHF range</p>'),
        required=False,
    )

    route_to_follow = RichText(
        title=_(u'Route to follow'),
        description=_(u'<p>Is it always the same, or according to the intervention, you must take into account the direction of the wind, or arrive by a particular access to the site according to the place where the event occurred</p>'),
        required=False,
    )

    site_particularities = RichText(
        title=_(u'Site Particularities'),
        description=_(u'<p>Describe in a few words why this site is special and has been the subject of a PPI.</p><p>Example: Access not very obvious, complex architecture, exceptional risk(s) present, means of control available on site for firefighters, place for which an intervention will be arduous because of the absence of compartmentalization...</p>'),
        required=False,
    )

    instructions_for_the_operator = RichText(
        title=_(u'Instructions for the operator'),
        description=_(u'<p>Specify here if specific actions are to be taken by the operator.</p><p>For example, if the call comes from a private individual, it is imperative to contact the lodge on duty to inform those in charge of the site of our arrival, and thus be welcomed.</p>'),
        required=False,
    )

    fieldset(
        'during the ride',
        label=_(u'3 During the ride'),
        fields=['vehicle_stop_emergency_reception_point',
                'point_of_first_destination',
                ]
    )

    vehicle_stop_emergency_reception_point = RichText(
        title=_(u'Vehicle stop/emergency reception point'),
        description=_(u'<p>Specify here if a meeting point is planned with site managers for reasons of access complexity, or if depending on a chemical scenario you should not get too close...</p>'),
        required=False,
    )

    point_of_first_destination = RichText(
        title=_(u'Point of First Destination (PFD)'),
        description=_(u'<p>Specify if a particular place has been designed to gather emergency services in the event of an increase in power. Important mainly if reflex reinforcements are sent, or in case of chemical intervention, for example.</p>'),
        required=False,
    )

    fieldset(
        'on_site',
        label=_(u'4 On site'),
        fields=['reflex_measurements_on_arrival_on_site',
                'special_means_of_protection_to_wear',
                'risks_present',
                'materials_equipment_available',
                ]
    )

    reflex_measurements_on_arrival_on_site = RichText(
        title=_(u'Reflex measurements on arrival on site'),
        required=False,
    )

    special_means_of_protection_to_wear = RichText(
        title=_(u'Special means of protection to wear'),
        description=_(u'<p>Specify here the means that must be taken in addition to firefighting, or the personal protective equipment imposed on an industrial site for example</p>'),
        required=False,
    )

    materials_equipment_available = RichText(
        title=_(u'Materials/Equipment available'),
        description=_(u'<p>Identify the main risks of the site. limit yourself to about 5 maximum.</p><p>Completeness = drown the fish!</p>'),
        required=False,
    )

    risks_present = RichText(
        title=_(u'Risks Present'),
        description=_(u"<p>we need to know what's available to assist us in intervention. It is not necessary to mention the presence of fire extinguishers or even reels intended for the PPE of the site. On the other hand, hydrants, dry or wet columns... must be mentioned.</p>"),
        required=False,
    )

    fieldset(
        'Return to normal',
        label=_(u'5 Return to normal'),
        fields=['attention_points_for_the_return_to_normal',
                ]
    )

    attention_points_for_the_return_to_normal = RichText(
        title=_(u'Attention points for the return to normal'),
        required=False,
    )

    fieldset(
        'additional_information',
        label=_(u'6 Additional information'),
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
        description=_(
            u'<p>mandatory if wind has an influence (toxic risk)</p>'),
        required=False,
    )

    appendix_map_of_the_location = ObjectField(
        title=_(u'Appendix : Map of the location'),
        description=_(
            u'<p>To do via the PPI carto app to put on line on the map.</p><ul><li>Locate accesses</li><li>Red/black area if known</li><li>Type google map with black box on the object </li></ul>'),
        schema=ILinkFileRowSchema,
        required=False,
    )

    appendix_implementation_plan = NamedBlobFile(
        title=_(u'Appendix : Implementation Plan'),
        description=_(
            u'<p>mandatory : do in A3 on the basis of the zonal canvas</p><ul><li>Wind dose</li><li>Access</li><li>(Sub-funds)</li><li>Scale</li><li>Legend of layout </li><li>Pictogram<ul><li>Keybox</li><li>Concierge</li><li>Exhaust installation</li><li>Fire detection station (or firefighter control station)</li><li>Sprinkler installation</li></ul></li><li>Localization of the crisis room of the ets</li></ul>'),
        required=True,
    )

    appendix_water_resources = ObjectField(
        title=_(u'Appendix : Water resources'),
        description=_(
            u'<p>mandatory to be printed from the PPI carto application</p>'),
        schema=ILinkFileRowSchema,
        required=True,
    )

    appendix_axonometric_view = NamedBlobFile(
        title=_(u'Appendix : Axonometric view'),
        required=False,
    )

    appendix_carroyer_plan = NamedBlobFile(
        title=_(u'Appendix : Carroyer plan'),
        description=_(
            u"<p>Mandatory if the size of the site does not fit within a 250m x 250m square. To do by the Carto team to put online on the PPI carto app.</p><p>If there is no 'not shown', indicate 'not shown'.</p>"),
        required=True,
    )

    appendix_description = NamedBlobFile(
        title=_(u'Appendix : Description'),
        description=_(
            u'<p>Free annex examples</p><ul><li>Facade photos</li><li>Level plan<ul><li>Scale</li><li>Wind dose</li><li>Compartments</li><li>Access</li><li>Pictogra<ul><li>Keybox</li><li>Concierge</li><li>Exhaust installation</li><li>Fire detection center</li><li>Sprinkler installation</li><li>Localization of the crisis room of the ets</li></ul></li><li>Construction<ul><li>Wall structure</li><li>Roof structure</li></ul></li></ul></li><li>Fire panel operation mode</li></ul>'),
        required=False,
    )

    fieldset(
        'Administration of PPI',
        label=_(u'7 Administration of PPI'),
        fields=['description',
                'date_of_last_modification',
                'deadline_for_searching_for_additional_information',
                'modification_history',
                'case_officer',
                'preventionist',
                'availability_of_paper_copies',
                'classification_for_risk_analysis',
                ]
    )

    description = schema.TextLine(
        title=_(u'PPI reference'),
        required=True,
    )

    date_of_last_modification = schema.Datetime(
        title=_(u'Date of last modification'),
        required=False,
    )

    deadline_for_searching_for_additional_information = schema.Date(
        title=_(u'Deadline for searching for additional information'),
        required=False,
    )

    modification_history = schema.List(
        title=_(u'Modification history'),
        required=False,
        value_type=ObjectField(
            title=_(u'History'),
            schema=IHistoryRowSchema
        ),
    )

    case_officer = schema.TextLine(
        title=_(u'case_officer'),
        required=False,
    )

    preventionist = schema.TextLine(
        title=_(u'Preventionist'),
        required=False,
    )

    availability_of_paper_copies = schema.Text(
        title=_(u'Availability of Paper Copies'),
        description=_(u'<p>Specify the places where it is necessary to have paper copies available </p><ul><li>DZHC</li><li>Fastest first aid station (several if the means must come from several stations)</li></ul>'),
        required=False,
    )

    classification_for_risk_analysis = schema.Choice(
        title=_(u'Classification for risk analysis'),
        vocabulary=u'rescuearea.core.vocabularies.classification',
        required=False,
    )


class Ppi(Container):
    implements(IPpi)


register_object_factories(IPpi)
