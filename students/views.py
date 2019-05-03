# Create your views here.
from csv import excel
import openpyxl

from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from students.forms import LoginForm


def front_page(request):
    return render(request, 'homepage.html')

def login_page(request):
    return render(request, 'front.html')

def insert_excel(request):
    if request.method == "POST":
        excel_files = request.FILES["excel_file"]
        wb = openpyxl.load_workbook(excel_files)
        worksheet = wb["Book1"]
        print(worksheet)
        render(request, 'homepage.html', {"worksheet": worksheet})

    return render(request, 'insertExcel.html')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        print("YES")
        if form.is_valid():
            user = form.cleaned_data['user']

    else:
        form = LoginForm()

    return render(request, 'front.html', {"form": form})


class UploadFileForm(forms.Form):
    file = forms.FileField()
