from django import template

register = template.Library()

@register.filter(name='mul')
def mul_number(value_1, value_2):
    """
    p1*p2
    """
    return float(value_1)*float(value_2)

@register.filter(name='sub')
def sub_number(value_1, value_2):
    """
    p1-p2
    """
    return float(value_1)-float(value_2)

