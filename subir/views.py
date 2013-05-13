from django.shortcuts import render_to_response
from subir.forms import FormFoto
from django.http import HttpResponseRedirect
from django.template import RequestContext


def foto_vista(request):
    if request.method == 'POST':
        print request.FILES
        formulario = FormFoto(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = FormFoto()
    ctx = {'formulario': formulario}
    return render_to_response('index.html', ctx, context_instance = RequestContext(request) )
