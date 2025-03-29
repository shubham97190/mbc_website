from import_export import resources

from members.models import SeasonMemberMapping


class SeasonMemberResource(resources.ModelResource):
    class Meta:
        model = SeasonMemberMapping
    # fields = ('season__name', 'member__name', 'member__name_on_tag')
