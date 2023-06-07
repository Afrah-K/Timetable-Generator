from django.db import models
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator

TIMINGS = (
    ('9:30 - 10:30', '9:30 - 10:30'),
    ('10:30 - 11:30', '10:30 - 11:30'),
    ('11:30 - 12:30', '11:30 - 12:30'),
    ('12:30 - 1:30', '12:30 - 1:30'),
    ('2:30 - 3:30', '2:30 - 3:30'),
    ('3:30 - 4:30', '3:30 - 4:30'),
    ('4:30 - 5:30', '4:30 - 5:30'),
    )

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    )

YEAR_SEM = (
    ('1st Year/ SEMESTER 1', '1st Year/ SEMESTER 1'),
    ('1st Year/ SEMESTER 2', '1st Year/ SEMESTER 2'),
    ('2nd Year/ SEMESTER 3', '2nd Year/ SEMESTER 3'),
    ('2nd Year/ SEMESTER 4', '2nd Year/ SEMESTER 4'),
    ('3rd Year/ SEMESTER 5', '3rd Year/ SEMESTER 5'),
    ('3rd Year/ SEMESTER 6', '3rd Year/ SEMESTER 6'),
    ('4th Year/ SEMESTER 7', '4th Year/ SEMESTER 7'),
    ('4th Year/ SEMESTER 8', '4th Year/ SEMESTER 8'),
    )

# Create your models here.
 
class Instructor(models.Model):
    
    Inst_ID = models.CharField(max_length=10)
    Instructor_Name = models.CharField(max_length=30)   
    
    def __str__(self):
        return f'{self.Inst_ID}-{self.Instructor_Name}'
    

class Timeslot(models.Model):
    
    Meet_ID = models.CharField(max_length=10)
    Slots = models.CharField(max_length=13, choices=TIMINGS)
    Days = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    
    def __str__(self):
        return f'{self.Meet_ID}-{self.Days}-{self.Slots}'
    
class Room(models.Model):
    
    Room_ID = models.CharField(max_length=10)
    Room_Capacity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'{self.Room_ID}-{self.Room_Capacity}'
   
class Programme(models.Model):
    
    School = models.CharField(max_length = 40, blank = True, null = True)
    Programme_ID = models.CharField(max_length=10)
    Programme_Name = models.CharField(max_length=40)
    Programme_YearandSemester = models.CharField(max_length=20, choices = YEAR_SEM)
    
    def __str__(self):
        return f'{self.School}-{self.Programme_ID}-{self.Programme_Name}-{self.Programme_YearandSemester}'
    
class Course(models.Model):
    
    Programme_ID = models.ManyToManyField(Programme)
    Programme_Name = models.ManyToManyField(Programme)
    Programme_YearandSemester = models.ManyToManyField(Programme)  
    Course_ID = models.CharField(max_length=10)
    Course_Name = models.CharField(max_length=40)   
    Course_Capacity = models.PositiveIntegerField(default=0)
    Course_Instructor = models.ManyToManyField(Instructor)
    
    def __str__(self):
        return f'{self.Programme_Name}-{self.Course_Name}'