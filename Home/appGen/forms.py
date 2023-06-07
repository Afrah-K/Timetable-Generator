from django import forms
from django.forms import ModelForm
from .models import *

class InstructorsForm(ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'
        
class TimeslotsForm(ModelForm):
    class Meta:
        model = Timeslot
        fields = '__all__'
        
class RoomsForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        
class ProgrammesForm(ModelForm):
    class Meta:
        model = Programme
        fields = '__all__'
        
class CoursesForm(ModelForm):
    
    Course_Instructor = forms.ModelMultipleChoiceField(queryset=Instructor.objects.all())
    Programme_Name = forms.ModelMultipleChoiceField(queryset=Programme.objects.all())
    class Meta:
        model = Course
        fields = ['Programme_Name','Course_ID', 'Course_Name', 'Course_Capacity','Course_Instructor']