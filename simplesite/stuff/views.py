from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from stuff.models import Thing
from stuff.forms import StuffForm


def all_stuff(request):
    stuff = Thing.objects.all()
    return render_to_response('stuff/index.html',
                                      {'stuff': stuff},
                      context_instance=RequestContext(request))

def thing_details(request, thing_id):
    thing = get_object_or_404(Thing, pk=thing_id)
    return render_to_response('stuff/thing_details.html',
                                                  {'thing': thing},
                                context_instance=RequestContext(request))

def create_stuff(request):
    if request.method == 'POST':
        form = StuffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stuff')
    else:
        form = StuffForm()
    return render_to_response('stuff/create_stuff.html',
                                                          {'form': form},
                                context_instance=RequestContext(request))

def edit_stuff(request, thing_id):
    thing = get_object_or_404(Thing, pk=thing_id)
    if request.method == 'POST':
        form = StuffForm(request.POST, instance=thing)
        if form.is_valid():
            form.save()
            return redirect('thing_details', thing_id)
    else:
        form = StuffForm(instance=thing)
    return render_to_response('stuff/edit_stuff.html',
                                                          {'form': form},
                                context_instance=RequestContext(request))

def delete_stuff(request, thing_id):
    thing = get_object_or_404(Thing, pk=thing_id)
    thing.delete()
    return redirect('stuff')
