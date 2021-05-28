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

@register.inclusion_tag('header-search-hit.html')
def header_search_hit(request, field, text):
    d = request.GET.copy()
    query_term = d['query']
    search_field = d['field']
    if search_field == 'all':
        search_field = field
    if query_term == "":
        isTextInclude = False
    else:
        isTextInclude = (query_term in text)
    if (field == search_field) & isTextInclude:
        class_tag = "search-hit"
    else:
        class_tag = ""
    
    field = field.capitalize()

    return {
        'class_tag':class_tag,
        'field':field,
    }

@register.inclusion_tag('search-hit.html')
def search_hit(request, field, text):
    d = request.GET.copy()
    query_term = d['query']
    search_field = d['field']

    if search_field == 'all':
        search_field = field

    if field == 'abstract-short':
        text = text[0:400] + " ..."
        text = text.split(" ")
        return {
            'query_term':query_term,
            'text':text,
        }
    elif field == search_field:
        text = text.split(" ")
        return  {
            'query_term':query_term,
            'text':text,
        }
    else:
        text = text.split(" ")
        return {
            'query_term':"",
            'text':text,
        } 