from django import template

register = template.Library()


@register.filter
def escape_replace(value):
    return value.replace(" ", "_&_&_")
