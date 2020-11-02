from django.contrib import admin

from applications.insta.models import InstaPost, InstaImage, HashTag

admin.site.register(InstaPost)
admin.site.register(InstaImage)
admin.site.register(HashTag)

