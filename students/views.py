# Create your views here.
import openpyxl
import sqlite3

from django import forms
from django.shortcuts import render
from students.forms import LoginForm
from django.contrib.auth.decorators import login_required

@login_required()
def front_page(request):
    normal = []
    if request.method == "POST" and request.FILES['excel_file']:
        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()

        print("Table created!")
        sql_create = """ CREATE TABLE IF NOT EXISTS students(
            NUMBER integer PRIMARY KEY AUTOINCREMENT,
            ROOMNO VARCHAR(4),
            BLOCK VARCHAR(3),
            STUDENT VARCHAR(30),
            MOBILE VARCHAR(20),
            ID VARCHAR(20)
        ) """

        cursor.execute(sql_create)
        print("Table created!")


        #sql_insert = """ INSERT INTO students VALUES("312", "A", "Melvin George Mathew", "0509940039", "2015A7PS0197U")"""
        #cursor.execute(sql_insert)
        #print("You just got posted son!")

        excel_files = request.FILES["excel_file"]
        wb = openpyxl.load_workbook(excel_files)
        worksheet = wb["Book1"]
        #print(worksheet.get_highest_column())
        for row in worksheet.rows:
            normal.append(row)
        for rows in normal:
            print(rows[1].value)
            sql_insert = "INSERT INTO students(ROOMNO, BLOCK, STUDENT, MOBILE, ID) VALUES('{0}', '{1}', '{2}', '{3}', '{4}')".format(rows[0].value, rows[1].value, rows[2].value, rows[3].value, rows[4].value)
            cursor.execute(sql_insert)
            print("Data added!")

        cursor.execute("SELECT * FROM students")
        res = cursor.fetchall()
        connection.commit()
        connection.close()
        return render(request, 'homepage.html', {'res': res})

    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()
    sql_create = """ CREATE TABLE IF NOT EXISTS students(
                NUMBER integer PRIMARY KEY AUTOINCREMENT,
                ROOMNO VARCHAR(4),
                BLOCK VARCHAR(3),
                STUDENT VARCHAR(30),
                MOBILE VARCHAR(20),
                ID VARCHAR(20)
            ) """

    cursor.execute(sql_create)
    cursor.execute("SELECT * FROM students")
    res = cursor.fetchall()
    connection.commit()
    connection.close()
    return render(request, 'homepage.html', {'res': res})


def login_page(request):
    return render(request, 'login.html')

@login_required()
def insert_excel(request):
    print("This is the insert Excel page")
    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()
    if request.method == "POST":
        data = request.POST.copy()
        room_no = data.get('roomNo')
        block = data.get('blockNo')
        student = data.get('studentName')
        mobile = data.get('mobileNo')
        id = data.get('studentID')
        print(room_no)
        sql_insert_single = "INSERT INTO students(ROOMNO, BLOCK, STUDENT, MOBILE, ID) VALUES('{0}', '{1}', '{2}', '{3}', '{4}')".format(room_no, block, student, mobile, id)
        cursor.execute(sql_insert_single)
        connection.commit()
        connection.close()
    return render(request, 'insertExcel.html')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        print("YES")
        if form.is_valid():
            user = form.cleaned_data['user']

    else:
        form = LoginForm()

    return render(request, 'login.html', {"form": form})

def upload_excel(request):
    print("Boss mode")

class UploadFileForm(forms.Form):
    file = forms.FileField()

class NameForm(forms.Form):
    room_no = forms.Field
    block = forms.CharField(max_length=100)
    student = forms.CharField(max_length=100)
    mobile = forms.CharField(max_length=100)
    id = forms.CharField(max_length=100)
