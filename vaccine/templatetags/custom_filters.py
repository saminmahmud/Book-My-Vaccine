from django import template

register = template.Library()
# (name='has_group')
# @register.filter
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


register.filter("has_group", has_group)