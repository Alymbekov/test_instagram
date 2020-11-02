from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class InstaPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="posts", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    @property
    def get_absolute_image_url(self):
        return f"{self.images.first()}"


class InstaImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='insta_images/')
    posts = models.ForeignKey(
        InstaPost, on_delete=models.CASCADE, related_name='images'
    )

    def __str__(self):
        return f"{self.image.url}"


class HashTag(models.Model):
    title = models.CharField(max_length=150)
    posts = models.ManyToManyField(InstaPost)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class ApplicationForm(models.Model):
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    check = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email}, {self.city}"

    @staticmethod
    def is_check_true(status):
        if status == 'on':
            return True
        else:
            return False
