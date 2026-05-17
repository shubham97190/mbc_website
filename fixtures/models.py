from django.db import models

# Create your models here.
from page.models import Page, BaseModel
from tournament.models import Tournament


class Fixtures(Page, BaseModel):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Fixtures Page"
        verbose_name_plural = "Fixtures Page"


class FixtureCategory(models.Model):
    """One category per Excel sheet, e.g. '40+ Teams Fixtures'."""
    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE,
        related_name='fixture_categories',
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Fixture Category"
        verbose_name_plural = "Fixture Categories"

    def __str__(self):
        return self.name


class FixtureCourt(models.Model):
    """One court block within a category."""
    category = models.ForeignKey(FixtureCategory, on_delete=models.CASCADE, related_name='courts')
    name = models.CharField(max_length=50)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Fixture Court"
        verbose_name_plural = "Fixture Courts"

    def __str__(self):
        return f"{self.category.name} – {self.name}"


class FixtureTeam(models.Model):
    """A team assigned to a court."""
    court = models.ForeignKey(FixtureCourt, on_delete=models.CASCADE, related_name='teams')
    team_number = models.CharField(max_length=20)
    pair_name = models.CharField(max_length=200)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.team_number} – {self.pair_name}"


class FixtureMatch(models.Model):
    """A single match within a court."""
    court = models.ForeignKey(FixtureCourt, on_delete=models.CASCADE, related_name='matches')
    match_number = models.PositiveSmallIntegerField()
    team1 = models.CharField(max_length=200)
    team2 = models.CharField(max_length=200)

    class Meta:
        ordering = ['match_number']

    def __str__(self):
        return f"Match {self.match_number}: {self.team1} vs {self.team2}"
