from django.db import models
class UserData(models.Model):
   full_name=models.CharField(max_length=20)
   email=models.EmailField()
   mobile = models.TextField(null=True, blank=True) 
   resume = models.FileField(upload_to='resumes/')
   password=models.TextField()

   def __str__(self)-> str:
       return self.full_name


class Recruiter(models.Model):
    company_name = models.CharField(max_length=255)
    recruiter_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    profile_image = models.ImageField(
        upload_to="recruiter_profiles/",
        default="recruiter_profiles/default.jpg"   # FIXED
    )

    def __str__(self):
        return self.recruiter_name




class Student(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100, default='Not specified')
    email = models.EmailField()
    shortlisted = models.BooleanField(default=False)

    def __str__(self):
        return self.name





