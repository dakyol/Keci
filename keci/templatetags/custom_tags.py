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

#@register.simple_tag
def search_hit_class(request, field, field_name, text):
    d = request.GET.copy()
    query = d[field]
    if query in text:
        field_class = "search-hit search-hit-"+field_name
    else:
        field_class = ""
    return {

    }


#@register.inclusion_tag('search-hit.html')
def search_hit(request, field, text, id):
    d = request.GET.copy()
    query = d[field]
    words = text.split(" ")
    return {
        'field':field,
        'query':query,
        'words':words,
        'id':id,
    }

#@register.inclusion_tag('search-hit.html')
def search_hit(request, field_name, input, value):
    d = request.GET.copy()
    field_query = d[field_name]
    if field_query in input:
        search_result = "search-hit search-hit-"+field_name
    else:
        search_result = ""
    words = input.split(" ")
    field_id = "field_id_sonra" #str(id)+"-abstract-full"
    return {
        'field':value,
        'field_query':field_query,
        'words':words,
        'search_result':search_result,
        'field_id':field_id,
    }



    