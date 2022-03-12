from django.utils.text import slugify


def generate_unique_slug(klass, title):
    origin_slug = slugify(title)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{origin_slug}-{numb}'
        numb += 1
    return unique_slug
