# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage

from collective.z3cform.select2.widget.widget import MultiSelect2FieldWidget
from plone.app.textfield import RichText
from plone.autoform import directives as form
from plone.dexterity.browser import add
from plone.dexterity.content import Container
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form import validator
from z3c.form import button
from zope import schema
from zope.component import provideAdapter
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
        fields=['date_time',
                'location',
                'nature_and_risk_involved',
                'impacted_items',
                ]
    )

    date_time = schema.TextLine(
        title=_(u'Dates and times'),
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

    form.widget(impacted_items=MultiSelect2FieldWidget)
    impacted_items = schema.List(
        title=_(u'Impacted items'),
        value_type=schema.Choice(
            title=_(u'Impacted items'),
            source='rescuearea.core.vocabularies.impacted_items',
        ),
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
        defaultFactory=default_translator(_(u'<p>PMA IN, PMA out</p>')),
        default_mime_type='text/html',
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

    multidiciplinary = RichText(
        title=_(u'Multidiciplinary'),
        defaultFactory=default_translator(_(
            u'<table border="1">'
            u'<tbody>'
            u'<tr>'
            u'<td>CCE</td>'
            u'<td>Préciser les personnes (disciplines) présentes, le lieu, la plage horaire, et le rôle.  Si pas, indiquer « néant ».</td>'
            u'</tr>'
            u'<tr>'
            u'<td>C100</td>'
            u'<td>&nbsp;</td>'
            u'</tr>'
            u'<tr>'
            u'<td>&nbsp;</td>'
            u'<td>&nbsp;</td>'
            u'</tr>'
            u'</tbody>'
            u'</table>'
        )),
        default_mime_type='text/html',
        required=False,
    )

    discipline1 = RichText(
        title=_(u'Discipline 1'),
        defaultFactory=default_translator(_(
            u'<table border="1">'
            u'<tbody>'
            u'<tr>'
            u'<td width="30%">Moyens ZHC sur place</td>'
            u'<td>- Moyens Humains :<br />- Matériel :<br />- Horaire :<br />- Localisation :<br />- Mission des intervenants :</td>'
            u'</tr>'
            u'<tr>'
            u'<td>Moyens organisateur sur place (pour info)</td>'
            u'<td></td>'
            u'</tr>'
            u'<tr>'
            u'<td>Moyens ZHC extra au poste de secours</td>'
            u'<td> préciser l\'horaire s\'il y en a!</td>'
            u'</tr>'
            u'</tbody>'
            u'</table>'
        )),
        default_mime_type='text/html',
        required=False,
    )

    discipline2 = RichText(
        title=_(u'Discipline 2'),
        defaultFactory=default_translator(_(
            u'<table border="1">'
            u'<tbody>'
            u'<tr>'
            u'<td width="30%">Localisation PS, PMA ...</td>'
            u'<td>&nbsp;</td>'
            u'</tr>'
            u'<tr>'
            u'<td>Moyens organisateur sur place (pour info)</td>'
            u'<td>&nbsp;</td>'
            u'</tr>'
            u'<tr>'
            u'<td>Moyens ZHC extra au poste de secours</td>'
            u'<td>&nbsp;</td>'
            u'</tr>'
            u'</tbody>'
            u'</table>'
        )),
        default_mime_type='text/html',
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
        defaultFactory=default_translator(_(
            u'<p>Communication multidisciplinaire M HAI P0?</p>'
            u'<ul>'
            u'<li>groupe écouté par</li>'
            u'<li>préciser l\'horaire</li>'
            u'</ul>')),
        default_mime_type='text/html',
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


class DefaultValueValidator(validator.SimpleFieldValidator):

    def validate(self, value):
        super(DefaultValueValidator, self).validate(value)
        if self.field.defaultFactory(self) == value.output.replace('&#13;\n', '').replace('</p><p/><p>', '</p><p></p><p>'):
            raise Invalid(
                _(u'It is necessary to change the default value')
            )


class DefaultValueValidator2(validator.SimpleFieldValidator):

    def validate(self, value):
        super(DefaultValueValidator2, self).validate(value)
        if self.field.defaultFactory(self) == value.output.replace('&#13;\n', '').replace('</p><p/><p>', '</p><p></p><p>'):
            raise Invalid(
                _(u'It is necessary to change the default value')
            )


validator.WidgetValidatorDiscriminators(
    DefaultValueValidator,
    field=IPpie['communication_radio'],
)

validator.WidgetValidatorDiscriminators(
    DefaultValueValidator2,
    field=IPpie['nature_and_risk_involved']
)


provideAdapter(DefaultValueValidator)
provideAdapter(DefaultValueValidator2)


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

    def required_default(self, group, field_name, data):
        field_object = group.fields[field_name].field
        if field_object.required:
            default_value = group.fields[field_name].field.defaultFactory
            value = getattr(data, field_name, None)

            if default_value == value:
                return True
        return False

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


register_object_factories(IPpie)
