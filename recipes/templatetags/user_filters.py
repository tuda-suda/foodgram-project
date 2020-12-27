from django import template, forms
from django.contrib.auth import get_user_model

from api.models import Subscription


register = template.Library()
User = get_user_model()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})

@register.filter(name='is_subscribed_to')
def is_subscribed_to(user, author):
    return Subscription.objects.filter(user=user, author=author).exists()