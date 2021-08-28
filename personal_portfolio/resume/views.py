from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
#from rest_framework.parsers import JSONParser
from django.contrib import messages
import os
import gc
import sys
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.method=='POST':
        return render(request, "portfolio/index.html")

    else:
        return render(request,"portfolio/index.html")

def contact(request):
    if request.method=='POST':
        return render(request, "portfolio/contact.html")

    else:
        return render(request,"portfolio/contact.html")

def resume(request):
    if request.method=='POST':
        return render(request, "portfolio/resume.html")

    else:
        return render(request,"portfolio/resume.html")
def projects(request):
    if request.method=='POST':
        return render(request, "portfolio/projects.html")

    else:
        return render(request,"portfolio/projects.html")