from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from django.contrib import messages

from file_manager.models import *
from .forms import *

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def main(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    folders = ImageFolder.objects.filter(parent__isnull=True).order_by('name')
    images =  Image.objects.filter(folder__isnull=True).order_by('name')

    return render(request, 'admin/file_manager/images/main.html',{'input_name':input_name,'folders':folders,'images':images})

@staff_member_required
def new_folder(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    form = CreateFolderForm()

    if request.POST:
        form = CreateFolderForm(request.POST)
        if form.is_valid():
            form.save()
            if input_name:
                return HttpResponseRedirect(reverse('admin_image_uploader',args=[input_name]) + "?" + request.META['QUERY_STRING'])
            else:
                return HttpResponseRedirect(reverse('admin_cke_image_uploader') + "?" + request.META['QUERY_STRING'])

    return render(request, 'admin/file_manager/images/new-folder.html',{'input_name':input_name,'form':form})

@staff_member_required
def upload_file(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    form = ImageUploadForm()

    if request.POST:
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                image = form.save()
                messages.success(request,'Image Uploaded.')

                if input_name:
                    return HttpResponseRedirect(reverse('admin_image_uploader',args=[input_name]) + "?" + request.META['QUERY_STRING'])
                else:
                    return HttpResponseRedirect(reverse('admin_cke_image_uploader') + "?" + request.META['QUERY_STRING'])
            except:
                messages.error(request,'Could not upload image.')

    return render(request, 'admin/file_manager/images/upload-file.html',{'input_name':input_name,'form':form})

@staff_member_required
def folder(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    folder = get_object_or_404(ImageFolder,id=kwargs['folder_id'])
    sub_folders = ImageFolder.objects.filter(parent=folder).order_by('name')
    images = Image.objects.filter(folder=folder).order_by('name')

    return render(request, 'admin/file_manager/images/folder.html',{'input_name':input_name,'folder':folder,'sub_folders':sub_folders,'images':images})

@staff_member_required
def new_sub_folder(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    folder = get_object_or_404(ImageFolder,id=kwargs['folder_id'])

    form = CreateFolderForm()

    if request.POST:
        form = CreateFolderForm(request.POST)
        if form.is_valid():
            new_folder = form.save(commit=False)
            new_folder.parent = folder
            new_folder.save()
            if input_name:
                return HttpResponseRedirect(reverse('admin_image_folder',args=[input_name,folder.id]) + "?" + request.META['QUERY_STRING'])
            else:
                return HttpResponseRedirect(reverse('admin_cke_image_folder',args=[folder.id]) + "?" + request.META['QUERY_STRING'])

    return render(request, 'admin/file_manager/images/new-sub-folder.html',{'input_name':input_name,'folder':folder,'form':form})

@staff_member_required
def upload_file_folder(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    folder = get_object_or_404(ImageFolder,id=kwargs['folder_id'])

    form = ImageUploadForm()

    if request.POST:
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                image = form.save(commit=False)
                image.folder = folder
                image.save()
                messages.success(request,'Image Uploaded.')
                if input_name:
                    return HttpResponseRedirect(reverse('admin_image_folder',args=[input_name,folder.id]) + "?" + request.META['QUERY_STRING'])
                else:
                    return HttpResponseRedirect(reverse('admin_cke_image_folder',args=[folder.id]) + "?" + request.META['QUERY_STRING'])
            except:
                messages.error(request,'Could not upload image.')

    return render(request, 'admin/file_manager/images/upload-file-folder.html',{'input_name':input_name,'folder':folder,'form':form})

@staff_member_required
def edit_file(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    image = get_object_or_404(Image,id=kwargs['file_id'])
    form  = ImageUploadForm(instance=image)

    if input_name:
        if image.folder:
            redirect_url = reverse('admin_image_folder',args=[input_name,image.folder.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_image_uploader',args=[input_name]) + "?" + request.META['QUERY_STRING']
    else:
        if image.folder:
            redirect_url = reverse('admin_cke_image_folder',args=[image.folder.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_cke_image_uploader') + "?" + request.META['QUERY_STRING']

    if request.POST:

        form = ImageUploadForm(request.POST,request.FILES,instance=image)

        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Image Updated.')

                return HttpResponseRedirect(redirect_url)

            except:
                messages.error(request,'Could not update image.')

    return render(request, 'admin/file_manager/images/edit-image.html',{'input_name':input_name,'form':form,'image':image})

@staff_member_required
def delete_file(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    image = get_object_or_404(Image,id=kwargs['file_id'])

    if input_name:
        if image.folder:
            redirect_url = reverse('admin_image_folder',args=[input_name,image.folder.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_image_uploader',args=[input_name]) + "?" + request.META['QUERY_STRING']
    else:
        if image.folder:
            redirect_url = reverse('admin_cke_image_folder',args=[image.folder.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_cke_image_uploader') + "?" + request.META['QUERY_STRING']

    try:
        image.delete()
        messages.success(request,'Image Deleted.')
    except:
        messages.error(request,'Could not delete image.')

    return HttpResponseRedirect(redirect_url)

@staff_member_required
def edit_folder(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    folder = get_object_or_404(ImageFolder,id=kwargs['folder_id'])
    form = CreateFolderForm(instance=folder)

    if input_name:
        if folder.parent:
            redirect_url = reverse('admin_image_folder',args=[input_name,folder.parent.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_image_uploader',args=[input_name]) + "?" + request.META['QUERY_STRING']
    else:
        if folder.parent:
            redirect_url = reverse('admin_cke_image_folder',args=[folder.parent.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_cke_image_uploader') + "?" + request.META['QUERY_STRING']

    if request.POST:

        form = CreateFolderForm(request.POST,request.FILES,instance=folder)

        if form.is_valid():

            try:
                form.save()
                messages.success(request,'Folder Updated.')

                return HttpResponseRedirect(redirect_url)

            except:
                messages.error(request,'Could not update folder.')

    return render(request, 'admin/file_manager/images/edit-folder.html',{'input_name':input_name,'folder':folder,'form':form,'file':file})

@staff_member_required
def delete_folder(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    folder = get_object_or_404(ImageFolder,id=kwargs['folder_id'])

    if input_name:
        if folder.parent:
            redirect_url = reverse('admin_image_folder',args=[input_name,folder.parent.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_image_uploader',args=[input_name]) + "?" + request.META['QUERY_STRING']
    else:
        if folder.parent:
            redirect_url = reverse('admin_cke_image_folder',args=[folder.parent.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_cke_image_uploader') + "?" + request.META['QUERY_STRING']

    try:
        folder.delete()
        messages.success(request,'Folder Deleted.')
    except:
        messages.error(request,'Could not delete folder.')

    return HttpResponseRedirect(redirect_url)
