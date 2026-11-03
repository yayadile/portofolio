"""Template tags buat fitur bahasa.

{% t 'nav_about' %}        -> string UI sesuai bahasa aktif
{% pick profile 'about' %} -> about_en kalau EN & terisi, else about (fallback ID)
"""
from django import template

from ..lang import tr

register = template.Library()


def _lang(context):
    request = context.get('request')
    lang = getattr(request, 'LANG', 'id') if request else 'id'
    return lang if lang in ('id', 'en') else 'id'


@register.simple_tag(takes_context=True)
def t(context, key):
    return tr(key, _lang(context))


@register.simple_tag(takes_context=True)
def pick(context, obj, field):
    if obj is None:
        return ''
    if _lang(context) == 'en':
        en_val = (getattr(obj, f'{field}_en', '') or '').strip()
        if en_val:
            return en_val
    return getattr(obj, field, '') or ''
