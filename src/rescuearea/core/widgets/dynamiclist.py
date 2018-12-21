from z3c.form.browser import textlines
from z3c.form.converter import BaseDataConverter
from z3c.form.interfaces import IDataConverter
from z3c.form.interfaces import NO_VALUE
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.interface import implements
from zope.interface import provider
from zope.schema.interfaces import ISequence

from rescuearea.core.widgets import interfaces


class DynamicListWidget(textlines.TextLinesWidget):
    implements(interfaces.IDynamicListWidget)

    def update(self):
        super(DynamicListWidget, self).update()
        self.allow_javascript('form_dynamiclist')

    def allow_javascript(self, javascript):
        """ Adds an allowed javascript to the list in the request """
        js_list = self.request.get('ces_javascript_allowed', [])
        js_list.append(javascript)
        self.request['ces_javascript_allowed'] = list(set(js_list))

    def extract(self):
        value = super(DynamicListWidget, self).extract()
        if value == NO_VALUE:
            return value
        if isinstance(value, basestring):
            return [value]
        return [v for v in value if v]


def dynamic_list_field_widget(field, request):
    return FieldWidget(field, DynamicListWidget(request))


@adapter(ISequence, interfaces.IDynamicListWidget)
@provider(IDataConverter)
class DataConverter(BaseDataConverter):

    def toWidgetValue(self, value):
        """See z3c.form.interfaces.IDataConverter"""
        if value is self.field.missing_value:
            return []
        return [v for v in value if v]

    def toFieldValue(self, value):
        """See z3c.form.interfaces.IDataConverter"""
        if value == u'':
            return self.field.missing_value
        return [v for v in value if v]
