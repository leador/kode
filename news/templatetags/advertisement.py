import random
from django import template
from news.models import Advertise

register = template.Library()


@register.inclusion_tag('news/templatetags/advertisement.html')
def show_advertisement():
    ids = []
    adv = Advertise.objects.filter(active=True)
    for i in adv:
        ids.append(i.id)
    random_adv_id = random.choice(ids)
    advert = Advertise.objects.get(id=random_adv_id)

    return {'advert': advert}
