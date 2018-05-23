import re

from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


# url tag to active menu tag converter
@register.simple_tag(takes_context=True)
def active_menu(context, pattern_or_urlname):
    try:
        pattern = '^' + reverse(pattern_or_urlname) + '$'
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if re.search(pattern, path):
        return 'active'
    return ''
