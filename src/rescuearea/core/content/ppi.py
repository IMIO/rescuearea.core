# -*- coding: utf-8 -*-

from Products.CMFPlone.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
from Products.Five.browser.metaconfigure import ViewMixinForTemplates
from Products.statusmessages.interfaces import IStatusMessage

from plone import api
from plone.app.layout.viewlets import ViewletBase
from plone.app.textfield import RichText
from plone.app.textfield.value import IRichTextValue
from plone.dexterity.browser import add, edit, view
from plone.dexterity.content import Container
from plone.indexer.decorator import indexer
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form import button
from zope import schema
from zope.interface import implements
from zope.component import queryUtility
from plone.registry.interfaces import IRegistry


from rescuearea.core import _
from rescuearea.core.content.object_factory import ObjectField
from rescuearea.core.content.object_factory import register_object_factories
from rescuearea.core.utils import default_translator


occupation_table_value = (
    u'<table border="1"><tbody><tr>'
    u'<td><h6>Lieu</h6></td>'
    u'<td><h6>00h00</h6></td>'
    u'<td><h6>04h00</h6></td>'
    u'<td><h6>06h00</h6></td>'
    u'<td><h6>08h00</h6></td>'
    u'<td><h6>09h00</h6></td>'
    u'<td><h6>10h00</h6></td>'
    u'<td><h6>12h00</h6></td>'
    u'<td><h6>14h00</h6></td>'
    u'<td><h6>18h00</h6></td>'
    u'<td><h6>12h00</h6></td>'
    u'<td><h6>21h00</h6></td>'
    u'<td><h6>23h00</h6></td>'
    u'</tr><tr>'
    u'<td>&nbsp;</td>'
    u'<td>&nbsp;</td>'
    u'<td>&nbsp;</td>'
    u'<td>&nbsp;</td>'
    u'<td>&nbsp;</td>'
    u'<td>&nbsp;</td>'
    u'<td>&nbsp;</td>'
    u'<td>&nbsp;</td>'
    u'<td>&nbsp;</td>'
    u'<td>&nbsp;</td>'
    u'<td>&nbsp;</td>'
    u'<td>&nbsp;</td>'
    u'<td>&nbsp;</td>'
    u'</tr></tbody></table>'
    u'<div class="page" title="Page 1"><p></p></div>'
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


class IKeysCodeAccessBadgeFieldsRowSchema(model.Schema):

    existence_keys_code_access_badge = schema.Bool(
        title=_(u'Existence of keys, code, access badge?'),
        required=False,
    )

    information = RichText(
        required=False,
        default_mime_type='text/html',
        defaultFactory=default_translator(_(
            u'<p>Description and usefulness of the keys :</p>'
            u'<p>Where the key is stored :</p>'
            u'<p>Number of copies :</p>'
        )),
    )

    last_key_check_date = schema.Date(
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
        label=_(u'Description sheet'),
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

    occupancy_schedule = RichText(
        title=_(u'Occupancy schedule'),
        description=_(u'<p>Specify night occupancy or not. Specify public occupation</p>'),
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

    type_of_activity = schema.TextLine(
        title=_(u'Type of activity'),
        description=_(u'<p>Factory, warehouse, store, MRPA... Public access, number of people, valid? autonomous? sleeping? Describe in a few lines what it is about.</p>'),
        required=False,
    )

    concierge_service = schema.Bool(
        title=_(u'Concierge Service?'),
        required=False,
    )

    contacts = RichText(
        title=_(u'Contacts'),
        required=False,
        defaultFactory=default_translator(_(
            u'<table border = "1">'
            u'<tbody>'
            u'<tr>'
            u'<td><strong>Priority</strong></td>'
            u'<td><strong>Function</strong></td>'
            u'<td><strong>Phone</strong></td>'
            u'<td><strong>Remark</strong></td>'
            u'</tr>'
            u'<tr>'
            u'<td>&nbsp;</td>'
            u'<td>&nbsp;</td>'
            u'<td>&nbsp;</td>'
            u'<td>&nbsp;</td>'
            u'</tr>'
            u'</tbody>'
            u'</table>'
        )),
        default_mime_type='text/html',
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

    keys_code_access_badge = ObjectField(
        title=_(u'Keys, code, access badge?'),
        description=_(u'If yes, describe utility'),
        schema=IKeysCodeAccessBadgeFieldsRowSchema,
        required=False,
    )

    date_of_update_of_the_description_sheet = schema.Date(
        title=_(u'Date of update of the description sheet'),
        required=False,
    )

    fieldset(
        'before departure',
        label=_(u'Before departure'),
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
        label=_(u'During the ride'),
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
        label=_(u'On site'),
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
        label=_(u'Return to normal'),
        fields=['attention_points_for_the_return_to_normal',
                ]
    )

    attention_points_for_the_return_to_normal = RichText(
        title=_(u'Attention points for the return to normal'),
        required=False,
    )

    fieldset(
        'additional_information',
        label=_(u'Additional information'),
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
        required=True,
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
        required=False,
    )

    appendix_axonometric_view = NamedBlobFile(
        title=_(u'Appendix : Axonometric view'),
        required=False,
    )

    appendix_carroyer_plan = NamedBlobFile(
        title=_(u'Appendix : Carroyer plan'),
        description=_(
            u"<p>Mandatory if the size of the site does not fit within a 250m x 250m square. To do by the Carto team to put online on the PPI carto app.</p><p>If there is no 'not shown', indicate 'not shown'.</p>"),
        required=False,
    )

    appendix_description = NamedBlobFile(
        title=_(u'Appendix : Description'),
        description=_(
            u'<p>Free annex examples</p><ul><li>Facade photos</li><li>Level plan<ul><li>Scale</li><li>Wind dose</li><li>Compartments</li><li>Access</li><li>Pictogra<ul><li>Keybox</li><li>Concierge</li><li>Exhaust installation</li><li>Fire detection center</li><li>Sprinkler installation</li><li>Localization of the crisis room of the ets</li></ul></li><li>Construction<ul><li>Wall structure</li><li>Roof structure</li></ul></li></ul></li><li>Fire panel operation mode</li></ul>'),
        required=False,
    )

    fieldset(
        'Administration of PPI',
        label=_(u'Administration of PPI'),
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

    date_of_last_modification = schema.Date(
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


class EditForm(edit.DefaultEditForm):
    template = ViewPageTemplateFile('templates/ppi_form_edit.pt')


class RenderWidget(ViewMixinForTemplates, BrowserView):
    index = ViewPageTemplateFile('templates/ppi_widget_edit.pt')


class AddForm(add.DefaultAddForm, BrowserView):
    portal_type = 'ppi'
    template = ViewPageTemplateFile('templates/ppi_form_add.pt')

    def updateFields(self):
        super(add.DefaultAddForm, self).updateFields()
        self.group_errors = []
        self.update_fieldset_classes()

    @button.buttonAndHandler(_('Save'), name='save')
    def handleAdd(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            self.handle_errors(errors)
            return
        # self.update_fieldset_classes()
        obj = self.createAndAdd(data)
        if obj is not None:
            # mark only as finished if we get the new object
            self._finishedAdd = True
            IStatusMessage(self.request).addStatusMessage(
                self.success_message, "info"
            )

    def handle_errors(self, errors):

        group_ids = []
        self.group_labels = {}
        for error in errors:
            name = error.form.__name__
            if name not in group_ids:
                group_ids.append(name)
                self.group_labels[name] = error.form.label

        self.group_errors = group_ids

        self.update_fieldset_classes()

    def get_fieldset_legend_class(self, group):
        if group.__name__ in self.group_errors:
            return "error"
        return ""

    def update_fieldset_classes(self):
        self.fieldset_class = {}
        for group in self.groups:
            self.fieldset_class[group.__name__] = self.get_fieldset_legend_class(group)

    def get_group_label(self, group):
        return self.group_labels[group]


class AddView(add.DefaultAddView):
    form = AddForm


class PpiView(view.DefaultView):

    def check_default_value(self, widget):
        if widget.field.defaultFactory:
            default = widget.value.output.replace('&#13;\n', '').replace('</p><p/><p>', '</p><p></p><p>')
            value = widget.field.defaultFactory(self)
            if default == value:
                return False
        return True

    def check_value(self, obj):
        fields = []
        for widget in obj.subform.widgets.values():
            if type(widget).klass == 'object-widget':
                if self.check_value(widget):
                    fields.append(widget)
            else:
                if widget.value:
                    if type(widget).klass == 'richTextWidget':
                        if self.check_default_value(widget):
                            fields.append(widget)
                    else:
                        fields.append(widget)
        if fields:
            return True
        return False

    def check_group(self, group):

        fields = []

        for widget in group.widgets.values():
            if type(widget).klass == 'object-widget':
                if self.check_value(widget):
                    fields.append(widget)
            else:
                if type(widget).klass == 'richTextWidget':
                    if self.check_default_value(widget):
                        fields.append(widget)
                else:
                    fields.append(widget)
        if fields:
            return True
        return False

    def get_values(self, group):

        fields = []

        for widget in group.widgets.values():
            if type(widget).klass == 'object-widget':
                if self.check_value(widget):
                    fields.append(widget)
            else:
                if widget.value:
                    if type(widget).klass == 'richTextWidget':
                        if self.check_default_value(widget):
                            fields.append(widget)
                    else:
                        fields.append(widget)

        return fields

    def get_groups(self):
        groups = []

        for group in self.groups:
            fields = []

            for widget in group.widgets.values():
                if type(widget).klass == 'object-widget':
                    if self.check_value(widget):
                        fields.append(widget)
                else:
                    if widget.value:
                        if type(widget).klass == 'richTextWidget':
                            if self.check_default_value(widget):
                                fields.append(widget)
                        else:
                            fields.append(widget)
            if fields:
                groups.append(group)

        return groups

    def show_label(self, widget, widget2):
        if type(widget).klass == 'object-widget':
            if widget2.value:
                return True
        return False


class IconsView(BrowserView):
    def __call__(self):
        field_with_icon = [['keys_code_access_badge', 'existence_keys_code_access_badge']]
        registry = queryUtility(IRegistry, default={})
        html = ''
        for field in field_with_icon:
            if type(field) == list:
                if getattr(getattr(self.context, field[0]), field[1]):
                    icon = registry.get('ppi_{0}'.format(field), '')
                    if icon:
                        html = '{0}<img src="{1}" height="42" width="42">'.format(html, '{0}/{1}'.format(api.portal.get().absolute_url(), icon))
            else:
                if getattr(self.context, field):
                    icon = registry.get('ppi_{0}'.format(field), '')
                    if icon:
                        html = '{0}<img src="{1}" height="42" width="42">'.format(html, '{0}/{1}'.format(api.portal.get().absolute_url(), icon))
        return html


class IconsViewlet(ViewletBase):
    def render(self):
        return self.context.restrictedTraverse('@@icons')()


@indexer(IPpi)
def searchable_text_address(object, **kw):
    result = [safe_unicode(object.Title()).encode('utf-8'),
              safe_unicode(object.Description()).encode('utf-8')]
    address = getattr(object, 'address', None)
    if address:
        fields = ['number', 'street', 'zip_code', 'commune', 'longitude', 'latitude']
        for field_name in fields:
            value = getattr(address, field_name, None)
            if type(value) is unicode:
                text = safe_unicode(value).encode('utf-8')
                result.append(text)
            elif IRichTextValue.providedBy(value):
                transforms = getToolByName(object, 'portal_transforms')
                text = transforms.convertTo(
                    'text/plain',
                    safe_unicode(value.raw).encode('utf-8'),
                    mimetype=value.mimeType,
                ).getData().strip()
                result.append(text)

    return ' '.join(result)


register_object_factories(IPpi)
