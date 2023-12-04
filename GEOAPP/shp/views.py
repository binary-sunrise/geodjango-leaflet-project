from django.shortcuts import render
from .models import Shp
from tiff.models import Tiff
from note.models import Note

# Create your views here.
def index(request):
    shp =Shp.objects.all()
    tiff =Tiff.objects.all()
    note =Note.objects.all()
    return render(request, 'index.html',{'shp':shp,'tiff':tiff,'note':note})