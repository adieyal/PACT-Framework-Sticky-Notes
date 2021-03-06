from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template
urlpatterns = patterns('',
    (r'^$', "stickynotes.views.wall", {}, "sticky_wall"),
    (r'^new_note/$', "django.views.generic.simple.direct_to_template", {'template' : 'stickynotes/add_note.html'}, "sticky_new_note"),
    (r'^ajax/post/$', "stickynotes.views.new_note", {}, "sticky_new_note_save"),
    (r'^ajax/update_position/$', "stickynotes.views.update_position", {}, "sticky_update_position"),
    (r'^ajax/(\d+)/delete/$', "stickynotes.views.delete", {}, "sticky_update_position"),
)
