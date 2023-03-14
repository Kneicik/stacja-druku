from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from .forms import FileUploadForm
import requests
import json
import os

def index(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def home(request):
    response = requests.get('http://192.168.0.27/api/job', params={'apikey': "C46964C92A8B40C0B331AB1AA5441C46"}).json()
    return render(request,'home.htm',{'response':response,})

def temp(request):
    temp = requests.get('http://192.168.0.27/api/printer/tool', params={'apikey': "C46964C92A8B40C0B331AB1AA5441C46"}).json()
    job = requests.get('http://192.168.0.27/api/job', params={'apikey': "C46964C92A8B40C0B331AB1AA5441C46"}).json()
    return render(request,'temp.htm',{'temp':temp, 'response':job,})

def upload_file(request):
    file = open("media/test.gcode", "rb")
    url = "http://192.168.0.27/api/files/local"
    header={"x-api-key" : 'C46964C92A8B40C0B331AB1AA5441C46'}
    response = requests.post(url, files = {"file": file}, headers = header)
    if response.ok:
        message = "Plik przesłano z powodzeniem!"
    else:
        message = "Błąd podczas transferu pliku!"   
    return render(request, 'upload_file.htm', {'message': message})

def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            uploaded_file_url = fs.url(filename)
            return HttpResponseRedirect(request.path_info)
    else:
        form = FileUploadForm()
    return render(request, 'upload.htm', {'form': form})
