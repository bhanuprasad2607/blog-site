from django.db import models
import uuid


class Tag(models.Model):
    tag_title = models.CharField(max_length=100, blank=True, null=True)
    tag_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False)

    def __str__(self, *args, **kwargs):
        return self.tag_title


class Post(models.Model):
    post_title = models.CharField(max_length=200, blank=True, null=True)
    post_tags = models.ManyToManyField(Tag)
    post_description = models.TextField(null=True, blank=True)
    post_published = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateTimeField(auto_now=True)
    post_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False)

    def __str__(self, *args, **kwargs):
        return self.post_title
