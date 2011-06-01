from django.views.generic.simple import direct_to_template
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from stickynotes import models

def wall(request, template="stickynotes/wall.html", extra_context=None):
    extra_context = extra_context or {}
    extra_context["notes"] = models.Note.objects.all()

    return direct_to_template(request, template=template, extra_context=extra_context)

def new_note(request):

    if request.method == "POST":
        note = models.Note.objects.create(
            text=request.POST["body"],
            name=request.POST["author"],
            color=request.POST["color"],
            x=0, y=0, z=0
        )
        return HttpResponse(note.id)
    else:
        raise Http404
    
def update_position(request):
    if request.method == "POST":
        id = request.POST["id"]
        note = get_object_or_404(models.Note, pk=id)
        note.x = int(request.POST["x"])
        note.y = int(request.POST["y"])
        note.z = int(request.POST["z"])
        note.save()

        return HttpResponse("")
    else:
        raise Http404
    
