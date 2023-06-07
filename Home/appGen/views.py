from django.shortcuts import render, HttpResponse, redirect
from .forms import * 
from django.http import JsonResponse
    
# Create your views here.

def home(request):
    return render(request,'home.html')

def instructors(request):
    form = InstructorsForm()
    if request.method == "POST":
        print(request.POST)
        form = InstructorsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/instructors')
    
    allinst = Instructor.objects.all()
    context = {'form':form, 'instructors_list' : allinst}
    print(allinst)
    return render(request,'instructors.html', context) 

def delInstructors(request, pk):
    get_inst = Instructor.objects.get(id = pk)
    get_inst.delete()
    return redirect('instructors')   

def timeslots(request):
    form = TimeslotsForm()
    if request.method == "POST":
        print(request.POST)
        form = TimeslotsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/timeslots')
    
    alltimes = Timeslot.objects.all()
    context = {'form':form, 'times_list' : alltimes}
    print(alltimes)
    return render(request,'timeslots.html', context)

def deltimeslots(request, pk):
    get_time = Timeslot.objects.get(id = pk)
    get_time.delete()
    return redirect('timeslots')

def rooms(request):
    form = RoomsForm()
    if request.method == "POST":
        print(request.POST)
        form = RoomsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/rooms')
    
    allrooms = Room.objects.all()
    context = {'form':form, 'rooms_list' : allrooms}
    print(allrooms)
    return render(request,'rooms.html', context) 

def delrooms(request, pk):
    get_rooms = Room.objects.get(id = pk)
    get_rooms.delete()
    return redirect('rooms')    

def programmes(request):
    form = ProgrammesForm()
    if request.method == "POST":
        print(request.POST)
        form = ProgrammesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/programmes')
    
    allprogrammes = Programme.objects.all()
    context = {'form':form, 'programmes_list' : allprogrammes}
    print(allprogrammes)
    return render(request,'programmes.html', context) 

def delprogrammes(request, pk):
    get_programmes = Programme.objects.get(id = pk)
    get_programmes.delete()
    return redirect('programmes')    

def courses(request):
    form = CoursesForm()
    if request.method == "POST":
        print(request.POST)
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'courses.html',context) 

def sections(request):
    return HttpResponse("This is the homepage(/)") 