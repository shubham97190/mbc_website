from django.urls import re_path
from file_manager.files import adminviews

urlpatterns = [

    re_path(r'^$', adminviews.main, name='admin_cke_file_uploader'),

    # from root
    re_path(r'^new-folder/$', adminviews.new_folder, name='admin_cke_file_new_folder'),
    re_path(r'^upload/$', adminviews.upload_file, name='admin_cke_file_upload_file'),

    # sub-folders
    re_path(r'^folder/(?P<folder_id>[-\d]+)/$', adminviews.folder, name='admin_cke_file_folder'),
    re_path(r'^folder/(?P<folder_id>[-\d]+)/new-folder/$', adminviews.new_sub_folder,
            name='admin_cke_file_new_sub_folder'),
    re_path(r'^folder/(?P<folder_id>[-\w]+)/upload/$', adminviews.upload_file_folder,
            name='admin_cke_file_upload_file_folder'),

    # deleting
    re_path(r'^file/(?P<file_id>[-\d]+)/edit/$', adminviews.edit_file, name='admin_cke_file_edit_file'),
    re_path(r'^file/(?P<file_id>[-\d]+)/delete/$', adminviews.delete_file, name='admin_cke_file_delete_file'),
    re_path(r'^folder/(?P<folder_id>[-\d]+)/edit/$', adminviews.edit_folder, name='admin_cke_file_edit_folder'),
    re_path(r'^folder/(?P<folder_id>[-\d]+)/delete/$', adminviews.delete_folder, name='admin_cke_file_delete_folder'),
]
