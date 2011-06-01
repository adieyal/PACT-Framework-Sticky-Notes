from django.views.generic.simple import direct_to_template
from django.http import HttpResponse

def wall(request, template="stickynotes/wall.html", extra_context=None):
    extra_context = extra_context or {}
    return direct_to_template(request, template=template, extra_context=extra_context)

def new_note(request):
    print request.POST
    return HttpResponse("43")
    
