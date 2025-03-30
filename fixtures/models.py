from django.db import models

# Create your models here.
from page.models import Page, BaseModel


class Fixtures(Page, BaseModel):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Fixtures Page"
        verbose_name_plural = "Fixtures Page"
