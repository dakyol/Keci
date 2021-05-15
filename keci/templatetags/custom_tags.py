from django import template

register = template.Library()

def split(value, arg):
    result = value.split(arg)
    return result

register.filter('split', split)