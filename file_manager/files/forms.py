from django.forms import ModelForm
from django import forms

from file_manager.models import *

class CreateFolderForm(ModelForm):

    class Meta:
        model = FileFolder
        exclude = ('parent',)

class FileUploadForm(ModelForm):

    class Meta:
        model = File
        exclude = ('folder',)
