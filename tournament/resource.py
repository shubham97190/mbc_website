from import_export import resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget, BooleanWidget

from tournament.models import Player, Tournament, TournamentCategory
from import_export.fields import Field

class YesNoBooleanWidget(BooleanWidget):
    def render(self, value, obj=None, **kwargs):
        # Convert True/False to "Yes"/"No" for export
        return "Yes" if value else "No"

    def clean(self, value, row=None, **kwargs):
        # Accept "Yes"/"No" strings as valid inputs during import
        if value in ["Yes", "yes", "YES"]:
            return True
        elif value in ["No", "no", "NO"]:
            return False
        return super().clean(value, row=row, **kwargs)

class PlayerResource(resources.ModelResource):
    tournament = Field(
        column_name='tournament',
        attribute='tournament',
        widget=ForeignKeyWidget(Tournament, field='name'))

    category = Field(
        column_name='category',
        attribute='category',
        widget=ManyToManyWidget(TournamentCategory, field='name', separator='|')
    )
    is_active = Field(
        column_name='Is Active',
        attribute='is_active',
        widget=YesNoBooleanWidget()
    )
    unisex_cap_order = Field(
        column_name='Unisex Cap Order',
        attribute='unisex_cap_order',
        widget=YesNoBooleanWidget()
    )
    terms_confirmed = Field(
        column_name='Terms & Conditions Acknowledged',
        attribute='terms_confirmed',
        widget=YesNoBooleanWidget()
    )
    opt_in = Field(
        column_name='Opt-In Consent',
        attribute='opt_in',
        widget=YesNoBooleanWidget()
    )
    facility_request = Field(
        column_name='Facility Request Acknowledged',
        attribute='facility_request',
        widget=YesNoBooleanWidget()
    )
    tournament_rules = Field(
        column_name='Tournament Rules Acknowledged',
        attribute='tournament_rules',
        widget=YesNoBooleanWidget()
    )
    

    class Meta:
        # fields = ('tournament__name', 'category__name')
        model = Player

        # fields = ['name', 'certificate_name', 'partner_name']
