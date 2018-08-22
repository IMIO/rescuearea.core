# encoding: utf-8

from zope.schema.vocabulary import SimpleVocabulary

from rescuearea.core import _


def dict_list_2_vocabulary(dict_list):
    """dict_list_2_vocabulary
    Converts a dictionary list to a SimpleVocabulary

    :param dict_list: dictionary list
    """
    terms = []
    for item in dict_list:
        for key in sorted([k for k in item]):
            terms.append(SimpleVocabulary.createTerm(
                key, str(key), item[key]))
    return SimpleVocabulary(terms)


class SEVESOVocabularyFactory(object):

    def __call__(self, context):
        values = [{'UNC': _('UNC', u'Unclassified')},
                  {'SMA': _('SMA', u'classified small SEVESO')},
                  {'BIG': _('BIG', u'classified big SEVESO')}]
        return dict_list_2_vocabulary(values)


SEVESOVocabulary = SEVESOVocabularyFactory()


class ClassificationVocabularyFactory(object):

    def __call__(self, context):
        values = [{'LOW': _('LOW', u'Low risk')},
                  {'MED': _('MED', u'Medium Risk')},
                  {'HIG': _('HIG', u'High risk')}]
        return dict_list_2_vocabulary(values)


ClassificationVocabulary = ClassificationVocabularyFactory()
