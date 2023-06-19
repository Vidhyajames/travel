from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team


def demo(request):
    obj=Place.objects.all()
    obj_team = Team.objects.all()

    return render(request,"index.html",{'result':obj,'res_team':obj_team})

# Create your views here.
