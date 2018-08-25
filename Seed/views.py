from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ImageExampleForm
from .retrain import run_inference_on_image
from mysite.settings import MEDIA_ROOT
import json
import time
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#폼추가

class GetJson:
    def __init__(self, DataJason):
        self.__DataJson = DataJason

    @property
    def DataJson(self):
        return self.__DataJson

    @DataJson.setter
    def DataJson(self, DATAJSON):
        self.__DataJson = DATAJSON

tempJson = GetJson({})

def GetJsonData(request):
    temp = request.POST.get('id',None)
    return HttpResponse(json.dumps(tempJson.DataJson), content_type="application/json")




def Seedimg(request):
    filename = "test.jpg"
    ImagePath = os.path.join(BASE_DIR, filename)
    return HttpResponse(ImagePath);

def handle_upload_file(f):
    tempPath = "C:/django/Seed/static/test"
    if f.name.split('.')[-1].upper() not in ['JPG','JPEG']:
        return 'ERROR'
    with open('{}.jpg'.format(tempPath), 'wb+') as w:
        for chunk in f.chunks():
            w.write(chunk)
    return '{}.jpg'.format(tempPath)


def ImageUpload(request):
    form = ImageExampleForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            handle_upload_file(request.FILES['image'])
            filename = "test.jpg"
            ImagePath = os.path.join("C:/django/Seed/static", filename)
            temp = run_inference_on_image(ImagePath)
            tempJson.DataJson = temp
            return render(request, 'Seed/ImageView.html', {'ImagePath' : ImagePath })

    return render(request, "Seed/ImageUpload.html", {'form' : form})



#def Image_Open(request):
#    if request.method == "POST":

# Create your views here.
