from django.template import RequestContext
from django.shortcuts import render_to_response


def home(request):
    context = {}
    return render_to_response('home.html', context, context_instance=RequestContext(request))
