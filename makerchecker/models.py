from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html


class MakerCheckerModel(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    maker = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='%(class)s_made', null=True, blank=True)
    checker = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='%(class)s_checked', null=True,
                                blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Make this an abstract model

    def __str__(self):
        return str(self.pk)  # Or any other identifying field
