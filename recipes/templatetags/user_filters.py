from django import template, forms


register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})

@register.filter(name='field_type')
def field_type(field):
    return field.field.widget.__class__.__name__