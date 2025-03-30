from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

STATUS = (
    ('', 'Status'),
    (0, 'In Process'),
    (1, 'Active'),
    (2, 'Completed'),
)


# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tournament Name", unique=True)
    title = models.CharField(max_length=100, verbose_name="Tournament Title", unique=True)
    tournament_date_time = models.DateTimeField(verbose_name="Tournament Date Time")
    last_registration_date = models.DateTimeField(verbose_name="Registration Last Date Time")
    venue = models.CharField(max_length=255, verbose_name="Venue")
    address = models.CharField(max_length=500, verbose_name="Address")
    total_allowed_registration = models.PositiveSmallIntegerField(verbose_name="Total Allowed Registration")
    status = models.PositiveIntegerField(choices=STATUS, verbose_name="Select Status")
    description = models.TextField(blank=True, null=True)
    term_condition = models.TextField(blank=True, null=True)
    is_current_active = models.BooleanField(default=False, verbose_name="Is Active")
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tournament_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tournament_updated_by")

    def __str__(self):
        return self.name


class TournamentCategory(models.Model):
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    fee = models.PositiveSmallIntegerField(blank=True, verbose_name="Fees")
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="category_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="category_updated_by")

    def __str__(self):
        return f"{self.name} - ${self.fee}"


class Player(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    category = models.ManyToManyField(TournamentCategory)

    name = models.CharField(max_length=255, verbose_name="Your Name")
    certificate_name = models.CharField(blank=True, max_length=255,
                                        verbose_name="Your Name on Certificate? Please leave empty "
                                                     "if Same as above")
    partner_name = models.CharField(max_length=255, verbose_name="Your partner name? If not confirmed please add NA")
    certificate_partner_name = models.CharField(blank=True, max_length=255, verbose_name="Your partner name on "
                                                                                         "Certificate? If not "
                                                                                         "confirmed please add NA or "
                                                                                         "leave empty "
                                                                                         "if Same as above")

    team_name = models.CharField(blank=True, max_length=255, verbose_name="Team Name? If not sure please add NA")
    mobile = PhoneNumberField(blank=True, region="CA",
                              verbose_name="Your mobile number (this would be used for WA messaging "
                                           "the tournament details)")
    email = models.CharField(blank=True, max_length=255)
    comments = models.CharField(blank=True, max_length=500, verbose_name="Any questions/ comments - please add.")
    unisex_cap_order = models.BooleanField(default=False, verbose_name="Unisex cap - white color/ black print")
    terms_confirmed = models.BooleanField()
    is_subscribe_for_email = models.BooleanField(default=True, verbose_name="Subscribes to Updates")
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player_updated_by")

    def __str__(self):
        return "{0} ({1})".format(self.name, self.partner_name)
