import uuid

from django.db import models
from django.db.models import Model, UUIDField

__all__ = ['CreatedModified']


class CreatedModified(Model):
    _id: UUIDField = models.UUIDField(primary_key=True, auto_created=True, editable=False, default=uuid.uuid4())
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
