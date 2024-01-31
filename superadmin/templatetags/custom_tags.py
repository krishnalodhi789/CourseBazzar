from django import template
import math
register = template.Library()

@register.filter(name="mul")
def mul(value, arg):
    res=float(value)*arg
    # print(type())
    print(type(arg))
    print(res)
    return res


@register.filter(name="div")
def div(value, arg):
    res=float(value)/arg

    return res