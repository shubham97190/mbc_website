from django import forms
from django.conf import settings
from django.db import models
from django.template.loader import render_to_string

from models import *

class ImageUploadWidget(forms.Widget):
    
    def render(self, name, value, attrs=None):
        if value:
            image = Image.objects.get(id=value)

        return render_to_string("admin/form/imageuploader.html", locals())
        
class ImageUploadField(models.ForeignKey):

    def __init__(self, *args, **kwargs):
        kwargs['blank'] = True
        kwargs['null'] = True
        kwargs['on_delete'] = models.SET_NULL
        super(ImageUploadField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ImageUploadWidget
        return super(ImageUploadField, self).formfield(**kwargs)
        
        
class FileUploadWidget(forms.Widget):
    
    def render(self,name,value,attrs=None):
        if value:
            file = File.objects.get(id=value)
        return render_to_string("admin/form/fileuploader.html",locals())
        
class FileUploadField(models.ForeignKey):
    
    def __init__(self,*args,**kwargs):
        kwargs['max_length'] = 200
        kwargs['blank'] = True
        kwargs['null'] = True
        kwargs['on_delete'] = models.SET_NULL
        super(FileUploadField,self).__init__(*args,**kwargs)
    
    def formfield(self,**kwargs):
        kwargs['widget'] = FileUploadWidget
        return super(FileUploadField,self).formfield(**kwargs)