from django import template

register = template.Library()

@register.filter(name = 'add_str')
def cut(value,arg):
    """
    This catenates the given arg string

    """
    val = str(value)
    return val + " " + arg

# register.filter('add_str',cut)
