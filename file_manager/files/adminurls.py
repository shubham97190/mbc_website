from django.conf.urls import *

urlpatterns = patterns('',

 	url(r'^(?P<input_name>[-\w]+)/$','file_manager.files.adminviews.main',name='admin_file_uploader'),

 	#from root
 	url(r'^(?P<input_name>[-\w]+)/new-folder/$','file_manager.files.adminviews.new_folder',name='admin_file_new_folder'),
 	url(r'^(?P<input_name>[-\w]+)/upload/$','file_manager.files.adminviews.upload_file',name='admin_file_upload_file'),

 	#sub-folders
 	url(r'^(?P<input_name>[-\w]+)/folder/(?P<folder_id>[-\d]+)/$','file_manager.files.adminviews.folder',name='admin_file_folder'),
 	url(r'^(?P<input_name>[-\w]+)/folder/(?P<folder_id>[-\d]+)/new-folder/$','file_manager.files.adminviews.new_sub_folder',name='admin_file_new_sub_folder'),
 	url(r'^(?P<input_name>[-\w]+)/folder/(?P<folder_id>[-\w]+)/upload/$','file_manager.files.adminviews.upload_file_folder',name='admin_file_upload_file_folder'),

 	#deleting
 	url(r'^(?P<input_name>[-\w]+)/file/(?P<file_id>[-\d]+)/edit/$','file_manager.files.adminviews.edit_file',name='admin_file_edit_file'),
 	url(r'^(?P<input_name>[-\w]+)/file/(?P<file_id>[-\d]+)/delete/$','file_manager.files.adminviews.delete_file',name='admin_file_delete_file'),
 	url(r'^(?P<input_name>[-\w]+)/folder/(?P<folder_id>[-\d]+)/edit/$','file_manager.files.adminviews.edit_folder',name='admin_file_edit_folder'),
 	url(r'^(?P<input_name>[-\w]+)/folder/(?P<folder_id>[-\d]+)/delete/$','file_manager.files.adminviews.delete_folder',name='admin_file_delete_folder'),


)
