from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveSmallIntegerField(default=18)
    post_history = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True,
        null=True, related_name='profiles'
    )

    def __str__(self):
        return f"{self.full_name}"


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} --> {self.last_name}"



