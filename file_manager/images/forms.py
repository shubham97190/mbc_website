from django.forms import ModelForm
from django import forms

from file_manager.models import *

class CreateFolderForm(ModelForm):

    class Meta:
        model = ImageFolder
        exclude = ('parent',)

class ImageUploadForm(ModelForm):

    class Meta:
        model = Image
        exclude = ('folder',)
