#---------------django imports----------------
from django.contrib import admin
from django.urls import include, path
from knox import views as knox_views

#---------------rest frameworks imports----------------
from rest_framework.routers import DefaultRouter

#---------------views imports----------------
from .views import LoginView, RegisterView, UserInfoView,ForgotEmailView

router = DefaultRouter()
router.register(r'user', UserInfoView)
router.register(r'user/<int:pk>/', UserInfoView)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(),name='register'),   
    path('login/', LoginView.as_view(),name='login'),  
    path('logout/', knox_views.LogoutView.as_view(),name='logout'),  
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('forgot_email/', ForgotEmailView.as_view(),name='email'),   
]