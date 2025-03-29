from django.db import models
from django.contrib.auth import get_user_model
from colorfield.fields import ColorField

STATUS = (
    ('', 'Status'),
    (1, 'Active'),
    (2, 'Completed'),
)

COLOR = [
    ('', 'Select Color'),
    ('#00FF00', 'Green'),
    ('#0000FF', 'Blue'),
    ('#FF0000', 'Red'),
    ('#FFFF00', 'Yellow'),
]

LEVEL = (
    ('', 'Select Level'),
    (1, 'Beginner'),
    (2, 'Intermediate'),
    (3, 'Upper Intermediate'),
    (4, 'Advanced'),
    (5, 'Competent'),
)


# Create your models here.
class Season(models.Model):
    name = models.CharField(max_length=50, verbose_name="Season Name", unique=True)
    is_current_active = models.BooleanField(default=False, verbose_name="Is this Current Season")
    status = models.PositiveIntegerField(choices=STATUS, verbose_name="Select Status")
    description = models.TextField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="season_created_by")
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="season_updated_by")

    def __str__(self):
        return "{0} ({1})".format(self.name, self.status)


class Member(models.Model):
    name = models.CharField(max_length=255, verbose_name="Full Name")
    email = models.CharField(max_length=255, unique=True)
    name_on_tag = models.CharField(max_length=255, unique=True)
    color = ColorField(choices=COLOR)
    level = models.PositiveSmallIntegerField(choices=LEVEL)
    is_active = models.BooleanField(default=True, verbose_name="Active")
    is_subscribe_for_email = models.BooleanField(default=True, verbose_name="Subscribes to Updates")
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="member_created_by")
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="member_updated_by")

    def __str__(self):
        return "{0} ({1})".format(self.name, self.name_on_tag)


class SeasonMemberMapping(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="mapping_created_by")
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="mapping_updated_by")

    class Meta:
        unique_together = ['season', 'member']
