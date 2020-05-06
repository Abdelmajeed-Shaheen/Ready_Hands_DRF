from django.urls import path
from .views import (RegisterAPI,
UserDetail,WorkerCreateAPI,ClientCreateAPI,
JobAPI,ServiceAPI,ClientJobAPI,JobApplicants,
CreateJobAPI,ApplyToJob,WorkerAppliedJobs,
AcceptWorker)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    #authentication
    path('login', TokenObtainPairView.as_view(), name='api-login'),
    path('register', RegisterAPI.as_view(), name='api-register'),
    path('worker/create/', WorkerCreateAPI.as_view(), name='api-worker-create'),
    path('client/create/', ClientCreateAPI.as_view(), name='api-client-create'),
    path('user/profile/', UserDetail.as_view(), name='api-user-profile'),
    #jobs
    path('jobs/', JobAPI.as_view(), name='api-jobs'),
    path('jobs/<int:job_id>/applicants/', JobApplicants.as_view(), name='api-client-job-applicants'),
    path('jobs/create/', CreateJobAPI.as_view(), name='api-client-create-job'),
    path('jobs/<int:job_id>/apply/', ApplyToJob.as_view(), name='api-worker-job-accept'),
    path('applicant/<int:applicant_id>/accept/', AcceptWorker.as_view(), name='api-applicant-accept'),
    path('worker/applied/jobs/', WorkerAppliedJobs.as_view(), name='api-worker-applied-jobs'),
    path('client/jobs/', ClientJobAPI.as_view(), name='api-client-jobs'),
    #services
    path('services/', ServiceAPI.as_view(), name='api-services'),
    ]
