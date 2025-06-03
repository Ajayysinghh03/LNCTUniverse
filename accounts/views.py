from .models import StudentProfile
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

@login_required
def student_profile(request):
    student = StudentProfile.objects.get(username=request.user.username)
    return render(request, 'accounts/students/student_profile.html', {'student': student})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student_dashboard')  # Redirect after login
    else:
        form = AuthenticationForm()
    
    return render(request, "accounts/students/student_login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return HttpResponse('successfully logged out') 
    
from django.shortcuts import render
from .models import StudentProfile, Timetable, Announcement

def dashboard(request): 
    timetable = Timetable.objects.all()
    announcements = Announcement.objects.all()
    return render(request, "accounts/students/student_dashboard.html", {
        "timetable": timetable,
        "announcements": announcements
    })

def fees(request):
    return HttpResponse("Fees page is under construction.")

def attendance(request):
    return HttpResponse("Attendance page is under construction.")