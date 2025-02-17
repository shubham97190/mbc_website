from django.urls import re_path
from file_manager.images import adminviews

urlpatterns = [

    re_path(r'^$', adminviews.main, {'template':'admin/image-uploader/main-cke.html'},name='admin_cke_image_uploader'),

    #from root
    re_path(r'^new-folder/$',adminviews.new_folder, name='admin_cke_image_new_folder'),
    re_path(r'^upload/$',adminviews.upload_file, name='admin_cke_image_upload_file'),

    #sub-folders
    re_path(r'^folder/(?P<folder_id>[-\d]+)/$', adminviews.folder, name='admin_cke_image_folder'),
    re_path(r'^folder/(?P<folder_id>[-\d]+)/new-folder/$', adminviews.new_sub_folder, name='admin_cke_image_new_sub_folder'),
    re_path(r'^folder/(?P<folder_id>[-\w]+)/upload/$', adminviews.upload_file_folder, name='admin_cke_image_upload_file_folder'),

    #deleting
    re_path(r'^file/(?P<file_id>[-\d]+)/edit/$', adminviews.edit_file,name='admin_cke_image_edit_file'),
    re_path(r'^file/(?P<file_id>[-\d]+)/delete/$', adminviews.delete_file,name='admin_cke_image_delete_file'),
    re_path(r'^folder/(?P<folder_id>[-\d]+)/edit/$', adminviews.edit_folder,name='admin_cke_image_edit_folder'),
    re_path(r'^folder/(?P<folder_id>[-\d]+)/delete/$', adminviews.delete_folder,name='admin_cke_image_delete_folder'),
]