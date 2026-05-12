from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import JsonResponse
from django.core.files.base import ContentFile
from .models import Recruiter
import base64
from django.views.decorators.csrf import csrf_exempt
from .models import UserData
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import Student
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .utils import send_shortlist_email 
from django import forms
from django.shortcuts import  redirect
from .forms import StudentForm
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')


def recruiter(request):
    return render(request,'recruiter.html')
    
def save_user(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        resume = request.FILES.get('resume')  

        user = UserData.objects.create(
            full_name=full_name,
            email=email,
            mobile=mobile,
            resume=resume,
            password=password
        )
        return render(request,'student_dashboard.html' , {"user": user})
    
    return render(request, 'login.html')

def student_dashboard(request):
    return render(request,'student_dashboard.html')
 
def cordinator(request):
    return render(request,'cordinator.html')

def verifier(request):
    return render(request,'verifier.html')

def active_job(request):
    return render(request,'active_job.html')

def candidate_search(request):
    return render(request,'candidate_search.html')

def analytics(request):
    return render(request,'analytics.html')

def interview(request):
    return render(request,'interview.html')

def notification(request):
    return render(request,'notification.html')

def postnew_job(request):
    return render(request,'postnew_job.html')

def recruiter_dashboard(request):
    return render(request,'recruiter_dashboard.html')

def job(request):
    return render(request,'job.html')

def candidate(request):
    return render(request,'candidate.html')

def profile(request):
    return render(request,'profile.html')

def applied_jobs(request):
    return render(request,'applied_jobs.html')

def thanks(request):
    return render(request,'thanks.html')

@csrf_exempt

def upload_photo(request):
    if request.method == "POST" and request.FILES.get("photo"):
        photo = request.FILES["photo"]

        # save file
        from django.core.files.storage import default_storage
        file_name = default_storage.save("profile_pics/temp.png", photo)
        file_url = default_storage.url(file_name)

        return JsonResponse({"image_url": file_url})

    return JsonResponse({"error": "Invalid request"})


@csrf_exempt
def delete_photo(request):
    if request.method != "POST":
        return JsonResponse({"status": "error", "message": "Invalid method"}, status=400)

    user = Recruiter.objects.first()   # FIXED

    user.profile_image.delete(save=False)
    user.profile_image = "recruiter_profiles/default.jpg"
    user.save()

    return JsonResponse({
        "status": "success",
        "image_url": user.profile_image.url
    })

@csrf_exempt
def send_student_email(request):
    if request.method == "POST":
        student_name = request.POST.get('name')
        try:
            student = Student.objects.get(name=student_name)
            send_shortlist_email(student.email, student.name)
            return JsonResponse({"status": "success", "message": f"Email sent to {student.name}"})
        except Student.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Student not found"})
    return JsonResponse({"status": "error", "message": "Invalid request"})





def notification (request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # database me save
            return redirect('/thanks.html')  # save ke baad redirect
    else:
        form = StudentForm()
    return render(request, "notification.html", {"form":form})
