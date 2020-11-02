from django.contrib import admin

from applications.insta.models import (
    InstaPost, InstaImage,
    HashTag, ApplicationForm)

admin.site.register(InstaPost)
admin.site.register(InstaImage)
admin.site.register(HashTag)
admin.site.register(ApplicationForm)

