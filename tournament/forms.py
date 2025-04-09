from django import forms
from django_select2.forms import Select2MultipleWidget
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from .models import Player, Tournament, TournamentCategory


class TournamentRegistrationForm(forms.ModelForm):
    required_css_class = 'required'
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    terms_confirmed = forms.BooleanField(required=True)
    facility_request = forms.BooleanField(required=True)
    tournament_rules = forms.BooleanField(required=True)
    category = forms.ModelChoiceField(
        queryset=TournamentCategory.objects.filter(is_active=True),
        widget=forms.RadioSelect(attrs={'id': 'id_category'})
    )

    def __init__(self, *args, **kwargs):
        super(TournamentRegistrationForm, self).__init__(*args, **kwargs)
        t: Tournament = Tournament.objects.filter(status=0, is_current_active=True)
        self.fields['tournament'].queryset = t
        self.fields['tournament'].initial = t and t.first().pk

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
            'opt_in',
            'terms_confirmed',
            'facility_request',
            'tournament_rules',
            'captcha',
        ]

        widgets = {
            'tournament': forms.TextInput(
                attrs={'id': 'id_tournament', 'class': 'form-control input-md', 'onChange': 'fetchDetails(this)',
                       'type': 'hidden'}),
            'category': forms.RadioSelect(attrs={'id': 'id_category'}),
            'name': forms.TextInput(
                attrs={'id': 'id_name', 'class': 'form-control input-md', 'placeholder': 'Your Name',
                       'onBlur': 'populateTeam(this.value)'}),
            'certificate_name': forms.TextInput(attrs={'id': 'id_certificate_name', 'class': 'form-control input-md',
                                                       'placeholder': 'Name on certificate (Leave empty if same as '
                                                                      'above)'}),
            'partner_name': forms.TextInput(attrs={'id': 'id_partner_name', 'class': 'form-control input-md',
                                                   'placeholder': 'Your Partner Name (add NA if not confirmed)'}),
            'certificate_partner_name': forms.TextInput(
                attrs={'id': 'id_certificate_partner_name', 'class': 'form-control input-md',
                       'placeholder': 'Partner Name on certificate (Leave empty if same as above)'}),
            'team_name': forms.TextInput(attrs={'id': 'id_team_name', 'class': 'form-control input-md',
                                                'placeholder': 'Team Name (add NA if not sure)'}),
            'mobile': RegionalPhoneNumberWidget(region="CA", attrs={'id': 'id_mobile', 'class': 'form-control input-md',
                                                                    'placeholder': 'Mobile Number',
                                                                    'onBlur': 'formatMobile()'}),
            'email': forms.EmailInput(
                attrs={'id': 'id_email', 'class': 'form-control input-md', 'placeholder': 'Email'}),
            'comments': forms.Textarea(
                attrs={'id': 'id_comments', 'class': 'form-control', 'placeholder': 'Any Questions/Comments',
                       'rows': 3, 'cols': 5}),
            'unisex_cap_order': forms.CheckboxInput(attrs={'id': 'id_unisex_cap_order', 'class': 'form-check-input'}),
            'opt_in': forms.CheckboxInput(attrs={'id': 'id_opt_in', 'class': 'form-check-input'}),
            'terms_confirmed': forms.CheckboxInput(attrs={'id': 'id_terms_confirmed', 'class': 'form-check-input'}),
            'facility_request': forms.CheckboxInput(attrs={'id': 'id_facility_request', 'class': 'form-check-input'}),
            'tournament_rules': forms.CheckboxInput(attrs={'id': 'id_tournament_rules', 'class': 'form-check-input'})
        }
