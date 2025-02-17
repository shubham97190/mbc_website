from django.db import models


# Create your models here.

class Enquiry(models.Model):
    ENQUIRER_TYPE_CHOICES = (
        ('', 'Enquiry Type'),
        (1, 'New Registration'),
        (2, 'Others'),
    )

    REFERRERAL_CHOICES = (
        ('', 'How Did You Hear About Milton Badminton Club?'),
        (1, 'Social Media'),
        (2, 'Website'),
        (3, 'Search Engine'),
        (4, 'Friend/Family or collegue'),
        (5, 'Other'),
    )

    first_name = models.CharField(max_length=100, verbose_name='First Name')
    surname = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=100)
    enquirer_type = models.PositiveIntegerField(choices=ENQUIRER_TYPE_CHOICES, verbose_name='Are you an')
    referrer = models.PositiveIntegerField(choices=REFERRERAL_CHOICES, verbose_name='How did you hear about Milton Badminton Club?')

    sector = models.CharField(max_length=100)
    message = models.TextField()
    added = models.DateTimeField(auto_now_add=True, editable=False)
    ip_address = models.CharField(max_length=100, editable=False)

    def __str__(self):
        return "%s [%s]" % (self.email, self.added)

    class Meta:
        verbose_name_plural = 'Enquiries'


class MagicBlueCircleEnquiry(models.Model):
    email = models.EmailField()
    interested_in_magic = models.BooleanField()
    interested_in_mbc = models.BooleanField()
    added = models.DateTimeField(auto_now_add=True, editable=False)
    ip_address = models.CharField(max_length=100, editable=False)

    def __str__(self):
        return "%s [%s]" % (self.email, self.added)

    class Meta:
        verbose_name_plural = 'Magic Blue Circle Enquiries'
