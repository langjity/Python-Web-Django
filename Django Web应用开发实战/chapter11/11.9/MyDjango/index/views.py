from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import Http404

def index(request):
    if request.GET.get('id', ''):
        raise Http404
    return render(request, 'index.html')

def myCookie(request):
    return HttpResponse('Done')


