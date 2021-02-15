from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    bad_words_list = ['бляд', 'хуй', 'пизд']
    for i in bad_words_list:
        if i.lower() in value.lower():
            value = value.lower().replace(i.lower(), '#$#%@%')
            break
    return str(value.capitalize())
