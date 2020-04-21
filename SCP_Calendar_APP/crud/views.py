from django.shortcuts import render, redirect, HttpResponse
from django.core import serializers
from django.db.models import DurationField, F, ExpressionWrapper
import datetime
from .models import BookList,Event,teacher_courses,students_courses

from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse


from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

import json
from django.contrib.auth.decorators import login_required


# Create your views here.
def userlogin(request):
    
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_staff and user.is_active :
                login(request,user)
                return redirect('/professor/')
            
            if user.is_active :
                login(request,user)
                return redirect('/student/')
      
            else:
                messages.error(request,'Username or password is incorrect. Please Try Again.')
                return redirect('/')
        else: 
            messages.error(request,'Username or password is incorrect.Please Try Again.')
            return redirect('/')
        
    else:
        return render(request,'login.html')

@login_required()
def index(request):
    events = teacher_courses.objects.all()
    context = {
        'events': events
    }
    return render(request, 'index.html', context)


def events(request):
    events = Event.objects.all().order_by('end')
    context = {
        'events': events
    }
    return render(request, 'events.html', context)

@login_required()
def student(request):
    events = Event.objects.all()
    

    
    alerts = Event.objects.raw('select id AS id, count(date(end)) AS alerts from crud_event where date(end) = CURDATE();')
    courseworks = Event.objects.raw('select  *  from crud_event where date(end) = CURDATE();')
    print(alerts)
    if alerts:
        context = {
            'events': events, 'alerts':alerts,'courseworks':courseworks
            }
    else: 
        context = {
            'events': events
            }

    return render(request, 'student.html', context)

def deadline(request):
    events = Event.objects.raw('SELECT id AS id,datediff(end,start) As days, datediff(end,start)*24 As hours, datediff(end,CURDATE()) AS daysleft, datediff(end,CURDATE())*24 AS dayslefthrs FROM crud_event')
     
    
    context = {
        'events': events
    }
    return render(request, 'deadline.html', context)


def create(request):
    print(request.POST)
    Course_Code = request.GET['Course_Code']
    Course = request.GET['Course']
    CW = request.GET['CW']
    title = request.GET['title']
    start = request.GET['start']
    end = request.GET['end']
    Description = request.GET['Description']

    if end  < start:
        messages.error(request,'Start date is greater than end date.')
        return redirect('/add_coursework/')

    else:
        book_details = Event(Course_Code=Course_Code,Course=Course, CW=CW,title=title, start=start,end=end,PART='-', Description=Description)
        book_details.save()
        return redirect('/events/')
    
    

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def add_book(request):
    return render(request, 'add_coursework.html')

def student_add(request):
    print(request.POST)
    title = request.GET['title']
    start = request.GET['start']
    end = request.GET['end']
    if end  < start:
        messages.error(request,'Start date is greater than end date.')

        return redirect('/studentAdd/')
        
    else:
        book_details = Event(title=title, start=start,end=end,PART='-',color='#888888')
        book_details.save()
        return redirect('/calendar/')
    


def studentAdd(request):
    return render(request, 'studentADD.html')


def edit(request, id):
    books = Event.objects.get(pk=id)
    context = {
        'books': books
    }
    return render(request, 'edit.html', context)


def update(request, id):
    books = Event.objects.get(pk=id)
    books.title = request.GET['title']
    books.Description = request.GET['Description']
    books.CW = request.GET['CW']
    books.start = request.GET['start']
    books.end = request.GET['end']
   
    if books.end  < books.start:
        return redirect('/professor/')
    else:
        books.save()
        return redirect('/events/')
    

def editColor(request, id):
    books = Event.objects.get(pk=id)
    context = {
        'books': books
    }
    return render(request, 'add_color.html', context)


def updateColor(request, id):
  
    books = Event.objects.get(pk=id)
    books.color = request.GET['color']

    books.save()
    return redirect('/student/')

def edit_task(request, id):
    books = Event.objects.get(pk=id)
    context = {
        'books': books
    }
    return render(request, 'edit_task.html', context)


def updateTask(request, id):
    books = Event.objects.get(pk=id)
    
    books.CW = request.GET['CW']
    books.PART = request.GET['PART']
    books.save()
    return redirect('/events/')

def calendar(request):
    events = eval(serializers.serialize("json", Event.objects.all()))
    #print(events[0])
    events = list(map(lambda x: x['fields'], events))
    print(events)
   
    # title =  Event.objects.all().values_list('title')
    # #print(events[0])
    
    # print(title)


    duration = Event.objects.raw('SELECT id AS id,datediff(end,start) As days, datediff(end,start)*24 As hours FROM crud_event')
    #print(events[0])
    
    print(duration)
 
    # events2 = Event.objects.filter(end-start)
   
    # print(events2)
   
    return render(request, 'calendar.html', context={'events': events,'duration':duration})