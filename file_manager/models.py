from django.db import models

class ImageFolder(models.Model):

    name = models.CharField(max_length=200)
    parent = models.ForeignKey('ImageFolder',null=True,blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_breadcrumbs(self):
        breadcrumbs = []
        breadcrumbs.append(self)
        if self.parent:
            parent_breadcrumbs = self.parent.get_parent_breadcrumbs(breadcrumbs)
            breadcrumbs.reverse()
            return breadcrumbs
        else:
            return breadcrumbs

    def get_parent_breadcrumbs(self,breadcrumbs):
        breadcrumbs.append(self)
        if self.parent:
            breadcrumbs = self.parent.get_parent_breadcrumbs(breadcrumbs)
            return breadcrumbs
        else:
            return breadcrumbs

class Image(models.Model):

    folder = models.ForeignKey('ImageFolder',null=True,blank=True,on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='resources/images')

    def __str__(self):
        return self.name

class FileFolder(models.Model):

    name = models.CharField(max_length=200)
    parent = models.ForeignKey('FileFolder',null=True,blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_breadcrumbs(self):
        breadcrumbs = []
        breadcrumbs.append(self)
        if self.parent:
            parent_breadcrumbs = self.parent.get_parent_breadcrumbs(breadcrumbs)
            breadcrumbs.reverse()
            return breadcrumbs
        else:
            return breadcrumbs

    def get_parent_breadcrumbs(self,breadcrumbs):
        breadcrumbs.append(self)
        if self.parent:
            breadcrumbs = self.parent.get_parent_breadcrumbs(breadcrumbs)
            return breadcrumbs
        else:
            return breadcrumbs

class File(models.Model):

    folder = models.ForeignKey('FileFolder',null=True,blank=True,on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='resources/files')

    def __str__(self):
        return self.name