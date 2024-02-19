from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def homepage(request):
    now = datetime.datetime.now() # 現在時間
    context = {'now':now}
    return render(request, 'homepage.html', context)