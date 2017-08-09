from __future__ import absolute_import

from django.http import HttpResponseRedirect

def home(request):
    return HttpResponseRedirect('vla/')


