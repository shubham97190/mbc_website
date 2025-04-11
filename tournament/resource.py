from import_export import resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from tournament.models import Player, Tournament, TournamentCategory
from import_export.fields import Field


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

    class Meta:
        # fields = ('tournament__name', 'category__name')
        model = Player

        # fields = ['name', 'certificate_name', 'partner_name']
