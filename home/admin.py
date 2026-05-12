from django.contrib import admin
from .models import UserData
from .models import Student
from .views import send_shortlist_email

# Register your models here.
admin.site.register(UserData)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if obj.shortlisted:
            send_shortlist_email(obj.email, obj.name)
