from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from .models import Enquiry, MagicBlueCircleEnquiry


class EnquiryForm(forms.ModelForm):
    # captcha = ReCaptchaField(label="Are you human?")
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        fields = ['first_name', 'surname', 'email', 'telephone', 'enquirer_type', 'referrer',
                  'message', 'captcha']
        model = Enquiry
        widgets = {
            'first_name': forms.TextInput(
                attrs={'id': 'id_first_name', 'class': 'form-control input-md', 'placeholder': 'First Name'}),
            'surname': forms.TextInput(
                attrs={'id': 'id_surname', 'class': 'form-control input-md', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(
                attrs={'id': 'id_email', 'class': 'form-control input-md', 'placeholder': 'Email'}),
            'telephone': forms.TextInput(
                attrs={'id': 'id_telephone', 'class': 'form-control input-md', 'placeholder': 'Telephone'}),
            'enquirer_type': forms.Select(attrs={'id': 'id_enquirer_type', 'class': 'form-control input-md', }),
            'referrer': forms.Select(attrs={'id': 'id_referrer', 'class': 'form-control input-md', }),
            'message': forms.Textarea(attrs={'id': 'id_message', 'class': 'form-control', 'placeholder': 'Message'}),
        }

    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)

        # self.fields['enquirer_type'] = forms.ChoiceField(choices=Enquiry.ENQUIRER_TYPE_CHOICES,
        # widget=forms.RadioSelect())


class MagicEnquiryForm(forms.ModelForm):
    # captcha = ReCaptchaField(label="Are you human?")
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        fields = ['email', 'interested_in_mbc', 'interested_in_magic', 'captcha']
        model = MagicBlueCircleEnquiry
        widgets = {
            'email': forms.TextInput(attrs={'id': 'id_email', 'class': 'form-control input-md', }),
        }
