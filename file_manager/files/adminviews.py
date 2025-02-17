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

    folders = FileFolder.objects.filter(parent__isnull=True).order_by('name')
    files =  File.objects.filter(folder__isnull=True).order_by('name')

    return render(request, 'admin/file_manager/files/main.html',{'input_name':input_name,'folders':folders,'files':files})

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
                return HttpResponseRedirect(reverse('admin_file_uploader',args=[input_name]) + "?" + request.META['QUERY_STRING'])
            else:
                return HttpResponseRedirect(reverse('admin_cke_file_uploader') + "?" + request.META['QUERY_STRING'])

    return render(request, 'admin/file_manager/files/new-folder.html',{'input_name':input_name,'form':form})

@staff_member_required
def upload_file(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    form = FileUploadForm()

    if request.POST:
        form = FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                file = form.save()
                messages.success(request,'File Uploaded.')

                if input_name:
                    return HttpResponseRedirect(reverse('admin_file_uploader',args=[input_name]) + "?" + request.META['QUERY_STRING'])
                else:
                    return HttpResponseRedirect(reverse('admin_cke_file_uploader') + "?" + request.META['QUERY_STRING'])
            except:
                messages.error(request,'Could not upload file.')

    return render(request, 'admin/file_manager/files/upload-file.html',{'input_name':input_name,'form':form})

@staff_member_required
def folder(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    folder = get_object_or_404(FileFolder,id=kwargs['folder_id'])
    sub_folders = FileFolder.objects.filter(parent=folder).order_by('name')
    files = File.objects.filter(folder=folder).order_by('name')

    return render(request, 'admin/file_manager/files/folder.html',{'input_name':input_name,'folder':folder,'sub_folders':sub_folders,'files':files})

@staff_member_required
def new_sub_folder(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    folder = get_object_or_404(FileFolder,id=kwargs['folder_id'])

    form = CreateFolderForm()

    if request.POST:
        form = CreateFolderForm(request.POST)
        if form.is_valid():
            new_folder = form.save(commit=False)
            new_folder.parent = folder
            new_folder.save()
            if input_name:
                return HttpResponseRedirect(reverse('admin_file_folder',args=[input_name,folder.id]) + "?" + request.META['QUERY_STRING'])
            else:
                return HttpResponseRedirect(reverse('admin_cke_file_folder',args=[folder.id]) + "?" + request.META['QUERY_STRING'])

    return render(request, 'admin/file_manager/files/new-sub-folder.html',{'input_name':input_name,'folder':folder,'form':form})

@staff_member_required
def upload_file_folder(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    folder = get_object_or_404(FileFolder,id=kwargs['folder_id'])

    form = FileUploadForm()

    if request.POST:
        form = FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            #try:
            file = form.save(commit=False)
            file.folder = folder
            file.save()
            messages.success(request,'File Uploaded.')
            if input_name:
                return HttpResponseRedirect(reverse('admin_file_folder',args=[input_name,folder.id]) + "?" + request.META['QUERY_STRING'])
            else:
                return HttpResponseRedirect(reverse('admin_cke_file_folder',args=[folder.id]) + "?" + request.META['QUERY_STRING'])
            #except:
            #    messages.error(request,'Could not upload file.')

    return render(request, 'admin/file_manager/files/upload-file-folder.html',{'input_name':input_name,'folder':folder,'form':form})

@staff_member_required
def edit_file(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    file = get_object_or_404(File,id=kwargs['file_id'])
    form  = FileUploadForm(instance=file)

    if input_name:
        if file.folder:
            redirect_url = reverse('admin_file_folder',args=[input_name,file.folder.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_file_uploader',args=[input_name]) + "?" + request.META['QUERY_STRING']
    else:
        if file.folder:
            redirect_url = reverse('admin_cke_file_folder',args=[file.folder.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_cke_file_uploader') + "?" + request.META['QUERY_STRING']

    if request.POST:

        form = FileUploadForm(request.POST,request.FILES,instance=file)

        if form.is_valid():
            try:
                form.save()
                messages.success(request,'File Updated.')

                return HttpResponseRedirect(redirect_url)

            except:
                messages.error(request,'Could not update file.')

    return render(request, 'admin/file_manager/files/edit-file.html',{'input_name':input_name,'form':form,'file':file})

@staff_member_required
def delete_file(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    image = get_object_or_404(File,id=kwargs['file_id'])

    if input_name:
        if image.folder:
            redirect_url = reverse('admin_file_folder',args=[input_name,image.folder.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_file_uploader',args=[input_name]) + "?" + request.META['QUERY_STRING']
    else:
        if image.folder:
            redirect_url = reverse('admin_cke_file_folder',args=[image.folder.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_cke_file_uploader') + "?" + request.META['QUERY_STRING']

    try:
        image.delete()
        messages.success(request,'File Deleted.')
    except:
        messages.error(request,'Could not delete file.')

    return HttpResponseRedirect(redirect_url)

@staff_member_required
def edit_folder(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    folder = get_object_or_404(FileFolder,id=kwargs['folder_id'])
    form = CreateFolderForm(instance=folder)

    if input_name:
        if folder.parent:
            redirect_url = reverse('admin_file_folder',args=[input_name,folder.parent.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_file_uploader',args=[input_name]) + "?" + request.META['QUERY_STRING']
    else:
        if folder.parent:
            redirect_url = reverse('admin_cke_file_folder',args=[folder.parent.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_cke_file_uploader') + "?" + request.META['QUERY_STRING']

    if request.POST:

        form = CreateFolderForm(request.POST,request.FILES,instance=folder)

        if form.is_valid():

            try:
                form.save()
                messages.success(request,'Folder Updated.')

                return HttpResponseRedirect(redirect_url)

            except:
                messages.error(request,'Could not update folder.')

    return render(request, 'admin/file_manager/files/edit-folder.html',{'input_name':input_name,'folder':folder,'form':form,'file':file})

@staff_member_required
def delete_folder(request,**kwargs):

    if 'input_name' in kwargs:
        input_name = kwargs['input_name']
    else:
        input_name = False

    folder = get_object_or_404(FileFolder,id=kwargs['folder_id'])

    if input_name:
        if folder.parent:
            redirect_url = reverse('admin_file_folder',args=[input_name,folder.parent.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_file_uploader',args=[input_name]) + "?" + request.META['QUERY_STRING']
    else:
        if folder.parent:
            redirect_url = reverse('admin_cke_file_folder',args=[folder.parent.id]) + "?" + request.META['QUERY_STRING']
        else:
            redirect_url = reverse('admin_cke_file_uploader') + "?" + request.META['QUERY_STRING']

    try:
        folder.delete()
        messages.success(request,'Folder Deleted.')
    except:
        messages.error(request,'Could not delete folder.')

    return HttpResponseRedirect(redirect_url)
