from django.urls import path
from .views import RegisterAPI,UserDetail,WorkerCreateAPI,ClientCreateAPI,JobAPI,ServiceAPI
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register', RegisterAPI.as_view(), name='api-register'),
    path('login', TokenObtainPairView.as_view(), name='api-login'),
    path('worker/create/', WorkerCreateAPI.as_view(), name='api-worker-create'),
    path('client/create/', ClientCreateAPI.as_view(), name='api-client-create'),
    path('user/profile/', UserDetail.as_view(), name='api-user-profile'),
    path('jobs/', JobAPI.as_view(), name='api-jobs'),
    path('services/', ServiceAPI.as_view(), name='api-services'),
    ]
