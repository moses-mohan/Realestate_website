from django import template

register = template.Library()


@register.filter
def inr(value):
    try:
        n = int(value)
    except (TypeError, ValueError):
        return value
    s = str(n)
    if len(s) <= 3:
        return s
    last3, rest = s[-3:], s[:-3]
    parts = []
    while len(rest) > 2:
        parts.insert(0, rest[-2:])
        rest = rest[:-2]
    if rest:
        parts.insert(0, rest)
    return ",".join(parts + [last3])