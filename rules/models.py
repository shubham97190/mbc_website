from django.db import models
from page.models import BaseModel


# Create your models here.

class Rules(BaseModel, models.Model):

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Rules'
        verbose_name_plural = 'Rules'
