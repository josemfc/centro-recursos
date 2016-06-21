from django import template

register = template.Library()

@register.filter(name="has_perm")
def has_perm(u, p):
    return u.has_perm(p)