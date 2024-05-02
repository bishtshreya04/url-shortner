from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse
def index(request):
# Create your views here.
    return render(request,'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5] if request.POST['alias'] == '' else request.POST['alias']
        new_url = Url.objects.create(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)
    
def go(request ,pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)