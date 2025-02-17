from django.conf.urls import *

urlpatterns = patterns('',

 	url(r'^(?P<input_name>[-\w]+)/$','file_manager.images.adminviews.main',name='admin_image_uploader'),

 	#from root
 	url(r'^(?P<input_name>[-\w]+)/new-folder/$','file_manager.images.adminviews.new_folder',name='admin_image_new_folder'),
 	url(r'^(?P<input_name>[-\w]+)/upload/$','file_manager.images.adminviews.upload_file',name='admin_image_upload_file'),

 	#sub-folders
 	url(r'^(?P<input_name>[-\w]+)/folder/(?P<folder_id>[-\d]+)/$','file_manager.images.adminviews.folder',name='admin_image_folder'),
 	url(r'^(?P<input_name>[-\w]+)/folder/(?P<folder_id>[-\d]+)/new-folder/$','file_manager.images.adminviews.new_sub_folder',name='admin_image_new_sub_folder'),
 	url(r'^(?P<input_name>[-\w]+)/folder/(?P<folder_id>[-\w]+)/upload/$','file_manager.images.adminviews.upload_file_folder',name='admin_image_upload_file_folder'),

 	#deleting
 	url(r'^(?P<input_name>[-\w]+)/file/(?P<file_id>[-\d]+)/edit/$','file_manager.images.adminviews.edit_file',name='admin_image_edit_file'),
 	url(r'^(?P<input_name>[-\w]+)/file/(?P<file_id>[-\d]+)/delete/$','file_manager.images.adminviews.delete_file',name='admin_image_delete_file'),
 	url(r'^(?P<input_name>[-\w]+)/folder/(?P<folder_id>[-\d]+)/edit/$','file_manager.images.adminviews.edit_folder',name='admin_image_edit_folder'),
 	url(r'^(?P<input_name>[-\w]+)/folder/(?P<folder_id>[-\d]+)/delete/$','file_manager.images.adminviews.delete_folder',name='admin_image_delete_folder'),

)
