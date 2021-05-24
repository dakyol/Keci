from django import template

register = template.Library()

def split(value, arg):
    result = value.split(arg)
    return result

register.filter('split', split)


@register.simple_tag
def url_replace(request, field, value):
    d = request.GET.copy()
    d[field] = value
    return d.urlencode()
    