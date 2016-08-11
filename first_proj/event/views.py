from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>It is now %s.</h1></body></html>" % now
    return render_to_response('events/index.html', {'date': now})

def date_ret(request, day=1):
    now = datetime.datetime.now() - datetime.timedelta(days=int(day))
    method = request.META['HTTP_USER_AGENT']
    return render(request, 'events/index.html', {'date': now, 'method': method})

def google(request):
    return redirect('http://google.kg')