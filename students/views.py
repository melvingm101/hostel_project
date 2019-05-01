# Create your views here.
from csv import excel

from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from students.forms import LoginForm


def front_page(request):
    return render(request, 'homepage.html')

def login_page(request):
    return render(request, 'front.html')

def insert_excel(request):
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

def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",
                                       file_name="download")
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        })

class UploadFileForm(forms.Form):
    file = forms.FileField()
