from django.shortcuts import render_to_response
from django.template import RequestContext
# from django.http import HttpResponse

def homepage(request):

    # return HttpResponse("ola")
    context = RequestContext(request)
    return render_to_response('index.html', context)
