from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Event(models.Model):
    #event, Holiday, Exam
    #description
    #heading
    #datetime


    CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4','4')
    )
    CHOICES1 = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D','D')
    )


   
    # CHOICES2 = (
    #     ('F21BD-CW1-PARTA', 'F21BD-CW1-PARTA'),
    #     ('F21BD-CW1-PARTB', 'F21BD-CW1-PARTB'),
    #     ('F21EC-CW1-PARTA', 'F21EC-CW1-PARTA')
    # )
    # CHOICES3 = (
    #     ('F21BD-CW1-PARTA', 'F21BD-CW1-PARTA'),
    #     ('F21BD-CW1-PARTB', 'F21BD-CW1-PARTB'),
    #     ('F21EC-CW1-PARTA', 'F21EC-CW1-PARTA')
    # )
    Course_Code=models.CharField( max_length=100)
    Course=models.CharField( max_length=100)
    CW=models.CharField(blank=True, null=True, choices=CHOICES,max_length=100, default='1')
    PART=models.CharField(blank=True, null=True, choices=CHOICES1,max_length=100, default='-')
    title = models.CharField( max_length=100)
    color = models.CharField(max_length=100,default='#00CC66')
    Description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    
    #all_day = models.BooleanField(default=False)


class teacher_courses(models.Model):
    department = models.CharField(max_length=150)
    Year=models.IntegerField()
    Course_Code=models.CharField( max_length=100)
    Course=models.CharField( max_length=100)

    def __str__(self):
        return self.department

class students_courses(models.Model):
    department = models.CharField(max_length=150)
    Year=models.IntegerField()
    Course_Code=models.CharField( max_length=100)
    Course=models.CharField( max_length=100)

    def __str__(self):
        return self.departmente