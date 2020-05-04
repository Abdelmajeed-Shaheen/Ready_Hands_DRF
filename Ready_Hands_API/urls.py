from django.urls import path
from .views import (RegisterAPI,
UserDetail,
WorkerCreateAPI,
ClientCreateAPI,
JobAPI,ServiceAPI,
ClientJobAPI,
JobApplicants,
CreateJobAPI,
ApplyToJob,
WorkerAppliedJobs)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register', RegisterAPI.as_view(), name='api-register'),
    path('login', TokenObtainPairView.as_view(), name='api-login'),
    path('worker/create/', WorkerCreateAPI.as_view(), name='api-worker-create'),
    path('client/create/', ClientCreateAPI.as_view(), name='api-client-create'),
    path('user/profile/', UserDetail.as_view(), name='api-user-profile'),
    path('jobs/', JobAPI.as_view(), name='api-jobs'),
    path('client/create/job/', CreateJobAPI.as_view(), name='api-client-create-job'),
    path('client/jobs/', ClientJobAPI.as_view(), name='api-client-jobs'),
    path('worker/applied/jobs/', WorkerAppliedJobs.as_view(), name='api-worker-applied-jobs'),
    path('client/job/<int:job_id>/applicants/', JobApplicants.as_view(), name='api-client-job-applicants'),
    path('worker/job/<int:job_id>/apply/', ApplyToJob.as_view(), name='api-worker-job-apply'),
    path('services/', ServiceAPI.as_view(), name='api-services'),
    ]
