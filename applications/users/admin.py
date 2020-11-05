from django.contrib import admin

from applications.users.models import (
    Profile, Person
)

admin.site.register(Profile)
admin.site.register(Person)
