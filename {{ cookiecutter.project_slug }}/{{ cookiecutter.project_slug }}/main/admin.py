from django.contrib import admin
{% if cookiecutter.remove_built_in_user_and_group_from_admin == 'y' %}
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)
{% endif %}
