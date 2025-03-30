from django import forms
from django_select2.forms import Select2MultipleWidget
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from .models import Player, Tournament


class TournamentRegistrationForm(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    def __init__(self, *args, **kwargs):
        super(TournamentRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['tournament'].queryset = Tournament.objects.filter(status=0, is_current_active=True)

    class Meta:
        model = Player
        fields = [
            'tournament',
            'category',
            'name',
            'certificate_name',
            'partner_name',
            'certificate_partner_name',
            'team_name',
            'mobile',
            'email',
            'comments',
            'unisex_cap_order',
            'terms_confirmed',
            # 'captcha',
        ]

        widgets = {
            'tournament': forms.Select(
                attrs={'id': 'id_tournament', 'class': 'form-control input-md', 'onChange': 'fetchDetails(this)'}),
            'category': Select2MultipleWidget(attrs={'id': 'id_category', 'class': 'form-control input-md'}),
            'name': forms.TextInput(
                attrs={'id': 'id_name', 'class': 'form-control input-md', 'placeholder': 'Your Name'}),
            'certificate_name': forms.TextInput(attrs={'id': 'id_certificate_name', 'class': 'form-control input-md',
                                                       'placeholder': 'Name on Certificate (Leave empty if same as '
                                                                      'above)'}),
            'partner_name': forms.TextInput(attrs={'id': 'id_partner_name', 'class': 'form-control input-md',
                                                   'placeholder': 'Your Partner Name (Add NA if not confirmed)'}),
            'certificate_partner_name': forms.TextInput(
                attrs={'id': 'id_certificate_partner_name', 'class': 'form-control input-md',
                       'placeholder': 'Partner Name on Certificate (Leave empty if same as above)'}),
            'team_name': forms.TextInput(attrs={'id': 'id_team_name', 'class': 'form-control input-md',
                                                'placeholder': 'Team Name (Add NA if not sure)'}),
            'mobile': forms.TextInput(
                attrs={'id': 'id_mobile', 'class': 'form-control input-md', 'placeholder': 'Your Mobile Number'}),
            'email': forms.EmailInput(
                attrs={'id': 'id_email', 'class': 'form-control input-md', 'placeholder': 'Email'}),
            'comments': forms.Textarea(
                attrs={'id': 'id_comments', 'class': 'form-control', 'placeholder': 'Any Questions/Comments'}),
            'unisex_cap_order': forms.CheckboxInput(attrs={'id': 'id_unisex_cap_order', 'class': 'form-check-input'}),
            'terms_confirmed': forms.CheckboxInput(
                attrs={'id': 'id_terms_confirmed', 'class': 'form-check-input'}),
        }
