#---------------django imports----------------
from django.contrib import admin
from django.urls import  path
from django.urls.conf import include

#---------------restframeworks imports----------------
from rest_framework.routers import DefaultRouter 

#---------------views imports----------------
from .views import CourseDetailsViews, CourseWishlistView

router = DefaultRouter()
router.register(r'courses', CourseDetailsViews)
router.register(r'courses/<int:pk>/', CourseDetailsViews)
router.register(r'wishlist', CourseWishlistView)
router.register(r'wishlist/<int:pk>', CourseWishlistView)

urlpatterns = [
    path('', include(router.urls)),
]