# -*- coding: utf-8 -*-
from collective.excelexport.exportables.dexterityfields import BaseFieldRenderer
from Products.CMFPlone.utils import safe_unicode
from plone import api
from plone.app.textfield.interfaces import IRichText
from rescuearea.core.content.ppi import IAddressRowSchema
from rescuearea.core.content.ppi import IKeysCodeAccessBadgeFieldsRowSchema
from rescuearea.core.content.ppi import ILinkFileRowSchema
from rescuearea.core.interfaces import IRescueareaCoreLayer
from zope.interface import Interface
from z3c.form.interfaces import NO_VALUE
from zope.component import adapts
from zope.i18n import translate
from zope.schema.interfaces import IObject
from zope.schema.interfaces import IText
from collective.excelexport.exportables.dexterityfields import TextFieldRenderer


class ObjectFieldRenderer(BaseFieldRenderer):
    adapts(IObject, Interface, Interface)

    def render_value(self, obj):
        values = self.get_value(obj)
        if IAddressRowSchema.providedBy(values):
            adresse = u"{0} {1}".format(self.get_num_street(values),
                                       self.get_zip_town(values))
            if self.get_coord(values):
                adresse = u"{0} ({1})".format(adresse,
                                             self.get_coord(values))
            return adresse

        if IKeysCodeAccessBadgeFieldsRowSchema.providedBy(values):
            return self.get_keys_code_access_badge(values)

        if ILinkFileRowSchema.providedBy(values):
            return self.get_link_file(values)

        return self.get_value(obj)

    def get_num_street(self, obj):
        if getattr(obj, 'number', None):
            try:
                return u"{0} {1}".format(obj.number, obj.street)
            except:
                __import__('pdb').set_trace()
        return obj.street

    def get_zip_town(self, obj):
        return u"{0} {1}".format(obj.zip_code, obj.commune)

    def get_coord(self, obj):
        if getattr(obj, 'longitude', None) or getattr(obj, 'latitude', None):
            return u"{0}/{1}".format(getattr(obj, 'longitude', ''),
                                     getattr(obj, 'latitude', ''))

    def get_keys_code_access_badge(self, obj):
        information = getattr(obj, 'information', None)
        last_key_check_date = getattr(obj, 'last_key_check_date', None)
        existence_keys_code_access_badge = obj.existence_keys_code_access_badge

        text = u"{0} : {1}".format(
            translate(u'Existence of keys, code, access badge?'),
            existence_keys_code_access_badge
        )

        if information:
            text = u"{0} \n{1}".format(
                text,
                self.get_richtext(information)
            )

        if last_key_check_date:
            text = u"{0} \n{1} : {2}".format(
                text,
                translate(u'Last Key Check Date'),
                last_key_check_date.strftime("%Y/%m/%d")
            )

        return text

    def get_richtext(self, value):
        ptransforms = api.portal.get_tool('portal_transforms')
        return ptransforms.convert('html_to_text', value.output).getData().strip()

    def get_file(self, value):
        return value and value.filename or u""

    def get_link_file(self, obj):
        file_obj = getattr(obj, 'file', None)
        link = getattr(obj, 'link', None)

        return u"{0} \n{1}".format(
            self.get_file(file_obj),
            link
        )


class FullTextFieldRenderer(TextFieldRenderer):
    adapts(IText, Interface, IRescueareaCoreLayer)

    def render_value(self, obj):
        """Gets the value to render in excel file from content value
        """
        value = self.get_value(obj)
        if not value or value == NO_VALUE:
            return ""

        text = safe_unicode(self._get_text(value))

        return text


class FullRichTextFieldRenderer(FullTextFieldRenderer):
    adapts(IRichText, Interface, IRescueareaCoreLayer)

    def _get_text(self, value):
        ptransforms = api.portal.get_tool('portal_transforms')
        return ptransforms.convert('html_to_text', value.output).getData().strip()
