from django.db import models
from django_extensions.db.fields import AutoSlugField

# Create your models here.
class Testapp(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(
        max_length=255,
        populate_from=['name'],
        editable=True,
        blank=True
    )
    description = models.TextField(blank=True, null=True)

