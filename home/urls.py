from django.urls import path
from .views import save_user
from . import views
from .views import notification
urlpatterns = [
    path("",views.index),
    path("login.html",views.login),
    path("recruiter.html",views.recruiter),
    path("student_dashboard.html",views.student_dashboard),
    path("cordinator.html",views.cordinator),
    path("verifier.html",views.verifier),
    path("active_job.html",views.active_job),
    path("candidate_search.html",views.candidate_search),
    path("analytics.html",views.analytics),
    path("interview.html",views.interview),
    path("notification.html",views.notification),
    path("postnew_job.html",views.postnew_job),
    path("recruiter_dashboard.html",views.recruiter_dashboard),
    path("job.html",views.job),
    path("candidate.html",views.candidate),
    path("profile.html",views.profile),
    path("upload_photo/", views.upload_photo, name="upload_photo"),
    path("delete_photo/", views.delete_photo, name="delete_photo"),
    path("save_user/", views.save_user, name="save_user"),
    path("applied_jobs.html",views.applied_jobs),
    path('send-email/', views.send_student_email, name='send_email'),
    path('notification./', views.notification, name='notification'),
    path("thanks.html",views.thanks),
]