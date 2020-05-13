from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def date_time_view(request):
    date=datetime.datetime.now()
    s='<h2> The current Date & Time of server is : '+ str(date)+ '</h2>'
    return HttpResponse(s)